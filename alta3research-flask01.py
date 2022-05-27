#!/usr/bin/env python3
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

app = Flask(__name__)



data = 
[
{"name" : "Chad"}
]

@app("/ jsondata")
def jsondata():
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)


