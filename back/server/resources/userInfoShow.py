import flask_restful
from flask_restful import reqparse
from flask_restful import fields, marshal_with, marshal
from ..models import User, OldProject
import json
import datetime

# resource_filed = {
#     'id': fields.Integer,
#     'phone': fields.String,
#     'username': fields.String,
#     'register_time': fields.String,
#     'email': fields.String,
#     'gender': fields.String,
#     'age': fields.Integer,
#     'good_at': fields.String,
#     'on_time': fields.Integer,
#     'credit': fields.Integer,
#     'quality': fields.Integer,
#     'price': fields.Integer,
#     'has_finish': fields.Integer,
#     'head_img': fields.String,
#     'old_project_list': fields.List
# }


class UserInfoShow(flask_restful.Resource):
    # @marshal_with(resource_filed)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='id is required')
        parser.add_argument('type', type=str, required=False)
        args = parser.parse_args()
        id = args['id']
        user = User.query.filter_by(id=id).first()
        if args['type'] is None:
            responseData = user.trans_to_dict()
        else:
            responseData = user.trans_to_dict()
        proList = list()
        for item in user.oldProject.all():
            proList.append(item.trans_to_dict())
        responseData['projectList'] = proList
        responseData['registerTime'] = responseData['registerTime'].strftime("%Y-%m-%d %H:%M:%S")
        print(responseData['registerTime'])
        return responseData
