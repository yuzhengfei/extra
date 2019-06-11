# todo 我的项目中进行时订单
import flask_restful
from flask_restful import reqparse
from flask_restful import fields, marshal_with, marshal
from ..models import ProOrder, ApplyPro, ReleasePro
from .. import db
import datetime


class HaveInHandListShow(flask_restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, required=True) # todo  用户id
        parser.add_argument('type', type=str, required=True, help='type is required')
        args = parser.parse_args()
        if args['type'] == '进行中':
            proOrderList = ProOrder.query.filter_by(employerId=args['id']).filter(ProOrder.status.endswith('中')).all()
            proOrderList.extend(ProOrder.query.filter_by(employeeId=args['id']).filter(ProOrder.status.endswith('中')).all())
        elif args['type'] == '已完成':
            proOrderList = ProOrder.query.filter_by(employerId=args['id']).filter(ProOrder.status.endswith('申诉完成')).all()
            proOrderList.extend(ProOrder.query.filter_by(employeeId=args['id']).filter(ProOrder.status.endswith('申诉完成')).all())
        elif args['type'] == '已冻结':
            proOrderList = ProOrder.query.filter_by(employerId=args['id']).filter(ProOrder.status.endswith('已冻结')).all()
            proOrderList.extend(ProOrder.query.filter_by(employeeId=args['id']).filter(ProOrder.status.endswith('已冻结')).all())
        proOrderList = sorted(proOrderList, key=lambda e: e.beginTime)
        releaseList = list()
        print(proOrderList)
        for orderItem in proOrderList:
            item = ReleasePro.query.filter_by(id=orderItem.releaseId, status=args['type']).first()
            if item is not None:
                item.releaseTime = item.releaseTime.strftime("%Y-%m-%d %H:%M:%S")
                item = item.trans_to_dict()
                item['orderId'] = orderItem.id
                releaseList.append(item)
        return releaseList
