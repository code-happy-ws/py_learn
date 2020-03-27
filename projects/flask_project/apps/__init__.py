from flask import Flask
from flask_cors import CORS
from flask_restful import Api


def creat_app():
    app = Flask(__name__)
    CORS(app)
    return app
