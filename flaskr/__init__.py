from flask import Flask
from config.Config import Config

# The __init__.py file initializes the package 'flaskr'. In this case, it just instantiates a Flask object.
app = Flask(__name__)
app.config.from_object(Config)

from flaskr import routes

