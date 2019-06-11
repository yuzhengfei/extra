# todo 注册

import flask_restful
from flask_restful import reqparse
from .. import db
from ..models import User
import random


class Register(flask_restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('phone', type=str, required=True, help='phone is required', location='form')
        parser.add_argument('userName', type=str, required=True, help='user Name is required', location='form')
        parser.add_argument('password', type=str, required=True, help='password is required', location='form')
        args = parser.parse_args()
        user = User(args['phone'], args['userName'], args['password'])
        db.session.add(user)
        db.session.commit()
        return '1'

