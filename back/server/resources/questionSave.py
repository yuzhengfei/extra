# todo 添加问题

import flask_restful
from flask_restful import reqparse
from .. import db
from ..models import Question
import random


class QuestionSave(flask_restful.Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId', type=int, required=True, help='userId is required')
        parser.add_argument('content', type=str, required=True, help='content is required')
        args = parser.parse_args()
        question = Question(args['userId'], args['content'])
        db.session.add(question)
        db.session.commit()
        return '1'

