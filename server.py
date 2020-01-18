from flask import Flask, redirect, url_for, render_template, request, session, flash,Response
from agora_community_sdk import AgoraRTC
# import models as dbHandler
from flask_sqlalchemy import SQLAlchemy



# Creating instance of Flask...
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)

# class User(db.Model):
# 	username = db.Column(db.String(40), primary_key = True, nullable=False)
# 	email = db.Column(db.String(100), unique=True, nullable=False)
# 	name = db.Column(db.String(), nullable=False)
# 	password = db.Column(db.String(), nullable=False)
#     phone = db.Column(db.String())
#     usertype = db.Column(db.String())
	


@app.route("/index")
def index():
    
    return render_template("index.html")

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        usertype = request.form.get('value')
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        contact = request.form['contact']
        # dbHandler.insertUser(name,username, password,usertype,email,contact)
        return redirect('index')
   		# users = dbHandler.retrieveUsers()



    return render_template('login.html')









if __name__ == '__main__':

	app.run(debug=True)

