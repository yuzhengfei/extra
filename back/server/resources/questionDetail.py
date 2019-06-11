import flask_restful
from flask_restful import reqparse
from flask_restful import fields, marshal_with, marshal
from ..models import User, ReleasePro, Answer, Question

# resource_filed = {
#     'id': fields.Integer,
#     'employerId': fields.Integer,
#     'projectName': fields.String,
#     'firstType': fields.String,
#     'secondType': fields.String,
#     'describe': fields.String,
#     'budget': fields.Integer,
#     'cycle': fields.String,
#     'company': fields.String,
#     'status': fields.String,
#     'releaseTime': fields.String,
#     'applyAmount': fields.Integer,
#     'browse': fields.Integer
# }


class QuestionDetail(flask_restful.Resource):
    # @marshal_with(resource_filed)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='id is required')
        args = parser.parse_args()

        # 获取问题相关信息
        question = Question.query.filter_by(id=args['id']).first()
        question.createTime = question.createTime.strftime("%Y-%m-%d %H:%M:%S")
        questitonUser = User.query.filter_by(id=question.userId).first()
        detailList = question.trans_to_dict()
        detailList['userId'] = questitonUser.id
        detailList['userName'] = questitonUser.userName
        detailList['headImg'] = questitonUser.headImg

        # 获取回答列表
        answerList = Answer.query.filter_by(questionId=args['id'])
        resultList = list()
        for answer in answerList:
            user = User.query.filter_by(id=answer.userId).first()
            answer.createTime = answer.createTime.strftime("%Y-%m-%d %H:%M:%S")
            answer = answer.trans_to_dict()
            answer['userId'] = user.id
            answer['userName'] = user.userName
            answer['headImg'] = user.headImg
            resultList.append(answer)
        # detailList = question.trans_to_dict()
        detailList['answerList'] = resultList
        return detailList