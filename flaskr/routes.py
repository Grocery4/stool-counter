from flask import render_template
from flaskr import app

@app.route("/")
#? do something


@app.route("/login")
def index():
    user = {
        'username' : 'TestUsername',
        'count' : 0
        }
    
    return render_template('login.html', title='Login page', user=user)