from flask_restful import Resource,reqparse,request
from flask import render_template,Response



class VueIndex(Resource):
    def get(self):
        return Response(render_template('vue_index.html'))