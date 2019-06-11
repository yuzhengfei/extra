import flask_restful
from flask_restful import reqparse
from flask_restful import fields, marshal_with, marshal
from ..models import User, ReleasePro

resource_filed = {
    'id': fields.Integer,
    'employerId': fields.Integer,
    'projectName': fields.String,
    'firstType': fields.String,
    'secondType': fields.String,
    'describe': fields.String,
    'budget': fields.Integer,
    'cycle': fields.String,
    'company': fields.String,
    'status': fields.String,
    'releaseTime': fields.String,
    'applyAmount': fields.Integer,
    'browse': fields.Integer,
    'integral': fields.Integer
}


class ShowReleasePro(flask_restful.Resource):
    @marshal_with(resource_filed)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True, help='id is required')
        args = parser.parse_args()
        releasePro = ReleasePro.query.filter_by(id=args['id']).first()
        releasePro.releaseTime = releasePro.releaseTime.strftime("%Y-%m-%d %H:%M:%S")
        return releasePro