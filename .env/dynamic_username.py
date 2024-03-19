from flask import Flask
from markupsafe import escape
app =Flask(__name__)
@app.route("/user/<user_name>")
def dynamic_username(user_name):
    return f"<h1>'my name is {user_name}.'</h1>"
app.run()
