from flask import Flask
from db import *
from routes import all_route
from flask_restful import Api
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

# initialize db
initialized_db(app)

#todo - creating routes

api = Api(app)
all_route(api)