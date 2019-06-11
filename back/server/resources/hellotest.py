import flask_restful
from flask import render_template


class Hello(flask_restful.Resource):
    def get(self):
        return 'dffdff'
