from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def root_route():
    return "Hello world!"

@app.route("/dojo")
def dojo_route():
    return "Dojo!"

@app.route("/say/<string:name>")
def hi_route(name):
    return f"Hi {name}"

@app.route("/say/<string:name>/<int:rep>")
def rep_route(name , rep):
    return f"Hi {name * rep}"



if __name__ == "__main__":
    app.run(debug=True)
