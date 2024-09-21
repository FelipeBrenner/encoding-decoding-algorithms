from flask import Flask, jsonify, request
from flask_cors import CORS

from coding import *

app = Flask(__name__)
cors = CORS(app, origins="*")


@app.route("/algorithms", methods=["GET"])
def algorithms():
  return jsonify({
    "algorithms": [
      {"key": "eliasgamma", "name": "Elias-Gamma"},
      {"key": "golomb", "name": "Golomb"},
    ]
  })


@app.route("/encode", methods=["POST"])
def encode():
  algorithm = request.json.get("algorithm")
  word = request.json.get("word")

  if algorithm == "eliasgamma":
    encoder = EliasGammaEncoding()
  elif algorithm == "golomb":
    encoder = GolombEncoding()
  else:
    return "Invalid algorithm selected.", 400

  codeword = [encoder.encode(s) for s in word]

  return jsonify({"codeword": codeword})


@app.route("/decode", methods=["POST"])
def decode():
  algorithm = request.json.get("algorithm")
  codeword = request.json.get("codeword")

  if algorithm == "eliasgamma":
    decoder = EliasGammaEncoding()
  elif algorithm == "golomb":
    decoder = GolombEncoding()
  else:
    return "Invalid algorithm selected.", 400

  try:
    word = [decoder.decode(c) for c in codeword]
  except:
    return "Unable to decode codeword using selected algorithm.", 400

  return jsonify({"word": ''.join(word)})


if __name__ == "__main__":
  app.run(debug=True, port=8080)
