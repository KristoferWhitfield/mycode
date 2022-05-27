#!/usr/bin/env python3
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import render_template
app = Flask(__name__)


# when making multi-line lists/dictionaries, the first brack must be on the same line as the variable. just a cute lil syntax rule -_-
yugiohcard = [ 
        {"monster name" : "blue eyes", 
 "level" : "8",
 "type" : "dragon", 
 "attribute" : "light",
 "atk" : "3000",
 "def" : "2500" }]

           # removed a whitespace between / and jsondata
@app.route("/jsondata")
def jsondata():
    return jsonify(yugiohcard)

@app.route("/")
def index(yugiohcard['monster name']):
    return render_template("textfile.html", monster = yugiohcard['monster name'] )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) 


