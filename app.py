from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    a = os.getenv("a")
    return a