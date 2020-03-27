from flask_restful import Resource,reqparse,request
from flask import render_template,Response



class BootstrapIndex(Resource):
    def get(self):
        return Response(render_template('table.html'))




