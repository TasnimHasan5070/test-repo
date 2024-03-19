from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello,My name is Prapty.I am so cute and beautiful</p>"
if "__main__"==__name__:
 app.run(debug=True)

