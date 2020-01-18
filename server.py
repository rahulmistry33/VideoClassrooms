from flask import Flask, redirect, url_for, render_template, request, session, flash
# Creating instance of Flask...
app = Flask(__name__)

@app.route("/index")
def index():
	return render_template("index.html")

if __name__ == '__main__':

	app.run(debug=True)

