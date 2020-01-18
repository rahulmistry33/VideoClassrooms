from flask import Flask, redirect, url_for, render_template, request, session, flash,Response
# from agora_community_sdk import AgoraRTC
# import models as dbHandler
from flask_sqlalchemy import SQLAlchemy
import os

# Creating instance of Flask...
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

db = SQLAlchemy(app)
app.secret_key = 'videoclassroom'

class User(db.Model):
    username = db.Column(db.String(40), primary_key = True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    contact = db.Column(db.String())
    usertype = db.Column(db.String())

@app.route("/index")
def index():
    return render_template("index.html")

def permit_login(username, password):
    try:
        user = User.query.filter_by(username=username).first()
        if user.password == password:
            print("Matched")
            session["username"] = username
            session["logged_in"] = True
            
            return redirect(url_for('dashboard'))
        else:
            return render_template("login.html")
    except:
        print("error")
        return redirect(url_for("login"))


@app.route('/dashboard')
def dashboard():
    print("Dashboard")
    return render_template("dashboard.html", username=session["username"])

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('index'))   
    return wrap

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        usertype = request.form.get('value')
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        contact = request.form['contact']
        user = User(username=username, email=email, name=name, password=password, contact=contact, usertype=usertype)
        db.session.add(user)
        db.session.commit()
        return redirect('index')
   		# users = dbHandler.retrieveUsers()
    return render_template('login.html')

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return permit_login(username,password)
    else:
        if 'logged_in' in session:
            return redirect(url_for('dashboard'))
        else:
            return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
