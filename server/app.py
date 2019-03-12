from flask import Flask, abort, request, jsonify
from classify_lyrics import classify_lyrics as classify



def create_app(test_config=None):
  app = Flask(__name__, instance_relative_config=True)

  if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
  else:
        # load the test config if passed in
        app.config.update(test_config)

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

  return app


if __name__ == '__main__':
  create_app().run(debug=True, host='0.0.0.0')
