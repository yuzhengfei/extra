# todo 问题列表

import flask_restful
from flask_restful import reqparse
from .. import db
from ..models import Question, User
import random


class QuestionList(flask_restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        # parser.add_argument('questionId', type=int, required=True, help='questionId is required')
        args = parser.parse_args()
        questionList = Question.query.all()
        resultList = list()
        for item in questionList:
            user = User.query.filter_by(id=item.userId).first()
            item.createTime = item.createTime.strftime("%Y-%m-%d %H:%M:%S")
            item = item.trans_to_dict()
            item['userId'] = user.id
            item['userName'] = user.userName
            item['headImg'] = user.headImg
            resultList.append(item)
        return resultList

