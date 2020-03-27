from flask_restful import Resource,reqparse,request
from flask import render_template,Response

parser=reqparse.RequestParser()
parser.add_argument('cases',type=str)
parser.add_argument('op',type=str)
parser.add_argument('username',type=str)
parser.add_argument('password',type=str)
parser.add_argument('repeatpasswd ',type=str)

class douban(Resource):
    def get(self):
        return Response(render_template('douban.html'))

    def post(self):
        args=parser.parse_args()
        cases=args.get('cases')
        return cases



