# todo 我的项目中发布中项目api，获取这两个类型的项目信息
import flask_restful
from flask_restful import reqparse
from flask_restful import fields, marshal_with, marshal
from ..models import User, ReleasePro
from .. import db


class MyProjectData(flask_restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='id is required')
        parser.add_argument('type', type=str, required=False)
        args = parser.parse_args()
        if args['type'] == 'releasing':
            return self.getReleasing(args['id'])

    def getReleasing(self, id):
        resultList = list()
        result = ReleasePro.query.filter_by(employerId=id, status='招募中').all()
        for item in result:
            item.releaseTime = item.releaseTime.strftime("%Y-%m-%d %H:%M:%S")
            resultList.append(item.trans_to_dict())
        return resultList
