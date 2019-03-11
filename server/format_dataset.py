import pandas as pd
from pathlib import Path
import string
import random

# Load data set, df = dataframe
df = pd.read_csv('lyrics.csv')
lyrics = df['lyrics']
labels = df[['name', 'artist']]

lyrics_training_set = []
# iterate over rows in lyrics.csv
# and create an array of 5 consecutive words from lyrics to train on
for index, row in df.iterrows():
  lyrics_str = row['lyrics']
  lyrics_str = lyrics_str.lower().translate(str.maketrans('', '', string.punctuation))
  lyrics_arr = lyrics_str.split()
  seperator = ' '
  lyrics_training_set_elem = []
  
  for i, elem in enumerate(lyrics_arr):
    lyrics_sub_arr = lyrics_arr[i:i+5]
    lyrics_sub_str = seperator.join(lyrics_sub_arr)
    lyrics_training_set_elem.append(lyrics_sub_str)
    # print(lyrics_sub_str)
  #end inner for
  
  lyrics_training_set.append(lyrics_training_set_elem)
  # print(index)
  # print(lyrics_str)
#end outer for

shuffled_lyrics_training_set = []
for index, lyrics in enumerate(lyrics_training_set):
    song_name = labels.loc[index]['name'].upper().replace(' ', '_')
    song_artist = labels.loc[index]['artist'].upper().replace(' ', '_')
    label = song_name + '+' + song_artist
    for elem in lyrics:
      fasttext_line = "__label__{} {}".format(label, elem)
      shuffled_lyrics_training_set.append(fasttext_line)
    # end inner for
  # end outer for
random.shuffle(shuffled_lyrics_training_set)

# What percent of data to save separately as test data
percent_test_data = 0.10

training_data = Path('lyrics_training_dataset.txt')
test_data = Path('lyrics_test_dataset.txt')

with training_data.open("w") as train_output, \
  test_data.open("w") as test_output:

  for fasttext_line in shuffled_lyrics_training_set:
    if random.random() <= percent_test_data:
      test_output.write(fasttext_line + "\n")
    else:
      train_output.write(fasttext_line + "\n")

# end with

# print(labels)


