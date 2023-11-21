from flask import Flask , render_template

app = Flask(__name__)


@app.route("/play")
def practice1():
    return render_template ("home.html", num=3, color="aqua")

@app.route("/play/<int:num>")
def practice2(num):
    return render_template ("home.html", num=num)

@app.route("/play/<int:num>/<string:color>")
def practice3(num, color):
    return render_template ("home.html", num=num, color=color)



if __name__ == "__main__":
    app.run(debug=True)
