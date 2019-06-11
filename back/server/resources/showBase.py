import flask_restful
from flask_restful import reqparse
from ..models import User


class ShowBase(flask_restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='id is required')
        args = parser.parse_args()
        user = User.query.filter_by(id=args['id']).first()
        print (args['id'])
        print(user.headImg)
        res = dict()
        res['headImg'] = user.headImg
        return res