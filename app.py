from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    a = os.getenv("a")
    return a