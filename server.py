from flask import Flask, redirect, url_for, render_template, request, session, flash,Response
from agora_community_sdk import AgoraRTC


# Creating instance of Flask...
app = Flask(__name__)

@app.route("/index")
def index():
    
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template('login.html')






if __name__ == '__main__':

	app.run(debug=True)

