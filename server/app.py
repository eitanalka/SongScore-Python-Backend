from flask import Flask, abort, request, jsonify
from classify_lyrics import classify_lyrics as classify

app = Flask(__name__)


@app.route('/')
def hello():
  return 'Hello'

@app.route('/classify-lyrics', methods=["POST"])
def classify_lyrics():
  if not request.json or not 'lyrics' in request.json:
    abort(400,'Must include lyrics field in body')
  lyrics = request.json['lyrics']
  response = classify(lyrics)
  return jsonify(response)


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
