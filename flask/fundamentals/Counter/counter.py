from flask import Flask, render_template, redirect, request, session

app= Flask(__name__)
app.secret_key='ahldkfgsdligsdohig'


@app.route("/")
def home():
    if "count" not in session:
        session["count"] = 0
    session["count"] += 1
    return render_template ("index.html")

@app.route("/request")
def request_info():
    session["count"] += 1
    return redirect ("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect ('/')

if __name__ == "__main__":
    app.run(debug=True)

