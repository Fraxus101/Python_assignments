from flask_app import app
from flask import render_template
from flask import request, redirect
from flask_app.models.friends import user

@app.route("/")
def home():
    return render_template("create.html")

@app.route("/display_friend/<int:id>")
def show_friend (id):
    data = {"id" : id}
    display_friend = user.select_friend(data)
    return render_template('show_friend.html' , friend = display_friend)

@app.route("/process", methods=["POST"])
def create():
    data = request.form
    user.create_friend(data)
    return redirect('/display_all')

@app.route("/display_all")
def display_all():
    all_friends = user.select_all()
    return render_template("read(all).html", friends = all_friends)
