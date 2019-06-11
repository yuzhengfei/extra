# 初始化app，restful api

from flask import Flask
import flask_restful
from flask_sqlalchemy import SQLAlchemy
from flask_cors import *


app = Flask(__name__)
CORS(app, supports_credentials=True)   # todo 允许跨域
api = flask_restful.Api(app)
app.config.from_object('config')
db = SQLAlchemy(app)



from . import views, models






