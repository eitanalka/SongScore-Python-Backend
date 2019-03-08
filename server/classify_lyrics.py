import fastText

def strip_formatting(string):
    return string.lower().replace('.', '').replace(',', '').strip()

def classify_lyrics(lyrics):
  preprocessed_lyrics = list(map(strip_formatting, lyrics))

  classifier = fastText.load_model('lyrics_model.bin')

  # classify lyrics 
  labels, probabilities = classifier.predict(preprocessed_lyrics, 1)

  # get the song and artist from the label
  song_artist = labels[0][0][9:].lower().replace('_', ' ')
  song_artist = song_artist.split('+')
  song = song_artist[0]
  artist = song_artist[1]

  return {
    'song': song,
    'artist': artist
  }

lyrics = [' Like it\'s dynamite']
print(classify_lyrics(lyrics))

# need to connect function to flask
