from flask import Flask
from markupsafe import escape
app=Flask(__name__)
element={"name":"python",
         "version":3.12
         }
@app.route('/user/<name>')
def user(name):
 return element["name"]
@app.route('/user/<version>')
def ver(version):
    return element["version"]
app.run()  

                     