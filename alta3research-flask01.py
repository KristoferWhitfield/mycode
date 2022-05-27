#!/usr/bin/env python3
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import render_template
app = Flask(__name__)



yugiohcard = 
[ {"monster name" : "blue eyes",
 "level" : "8",
 "type" : "dragon", 
 "attribute" : "light",
 "atk" : "3000",
 "def" : "2500" }]


@app.route("/ jsondata")
def jsondata():
    return jsonify(yugiohcard)

@app.route("/")
def index():
    return render_template("textfile.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)


