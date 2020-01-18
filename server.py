from flask import Flask, redirect, url_for, render_template, request, session, flash
# Creating instance of Flask...
app = Flask(__name__)

@app.route("/index")
def index():
	return render_template("index.html")

if __name__ == '__main__':
<<<<<<< HEAD
	app.run(debug=True)
=======
	app.run(debug=True)
>>>>>>> ae21041a0b886060ee2a2223f5ed90681d0f4ca8
