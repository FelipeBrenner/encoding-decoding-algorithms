from flask import Flask, jsonify, request
from flask_cors import CORS

import services
from coding import *

app = Flask(__name__)
cors = CORS(app, origins="*")


@app.route("/", methods=['GET'])
def hello_world():
	return jsonify({'hello': 'world'}), 201


@app.route("/algorithms", methods=["GET"])
def algorithms():
	return jsonify({
		"algorithms": services.ALGORITHM_REGISTRY
	})


@app.route("/encode", methods=["POST"])
def encode():
	try:
		algorithm = request.json.get("algorithm")
		word = request.json.get("word")
		params = {k: v for k, v in request.json.items() if k != 'algorithm' and k != "word"}
		coding: Coding = services.create_coding(algorithm, params)

		codeword = [services.encode(c, coding) for c in word]

		return jsonify({"codeword": codeword})
	except ValueError as e:
		return jsonify({"error": str(e)}), 400
	except TypeError as e:
		return jsonify({"error": f"Invalid payload ({str(e)})"}), 400


@app.route("/decode", methods=["POST"])
def decode():
	try:
		algorithm = request.json.get("algorithm")
		codeword = request.json.get("codeword")
		params = {k: v for k, v in request.json.items() if k != 'algorithm' and k != "codeword"}
		coding: Coding = services.create_coding(algorithm, params)

		word = [services.decode(s, coding) for s in codeword]

		return jsonify({"word": word})
	except ValueError as e:
		return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
	app.run(debug=True, port=8080)
