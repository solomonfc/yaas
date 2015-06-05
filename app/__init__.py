from flask import Flask
from flask.ext.restful import Api, Resource, reqparse, fields, marshal
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__,static_url_path="")
app.config.from_object('config')
db = SQLAlchemy(app)

from app import models, views, controllers