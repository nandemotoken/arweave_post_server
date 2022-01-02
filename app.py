from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    a = os.getenv("a")
    return a

@app.route('/post' , methods=["POST"])
def arpost():
    c = request.json["myfile"]
    return c




