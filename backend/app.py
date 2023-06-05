from flask import Flask, Response, jsonify, request
import numpy as np
from .errors import errors

app = Flask(__name__)
app.register_blueprint(errors)


@app.route("/")
def index():
    return Response("Hello, This is Flask API that takes a sentence as input and returns a random 500 dimensional array of floats.", status=200)


@app.route("/getEmbedding", methods=["POST"])
def custom():
    payload = request.get_json()

    if payload.get("sentence"):
        arr = np.random.rand(1,500)[0].tolist()
        obj = {"message":"success","data":arr}
        output = jsonify(obj)
    else:
        obj = {"message":"Error in Generating array","data":""}
        output = jsonify(obj)

    return output


@app.route("/health")
def health():
    return Response("OK", status=200)
