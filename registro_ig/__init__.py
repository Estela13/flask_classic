from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")

from registro_ig.routes import *