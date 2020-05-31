from flask_restful import Api

from apps.Vue.views import VueIndex
from apps.bootstrap.views import  BootstrapIndex


api = Api()

def init_app(app):
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    api.init_app(app)

api.add_resource(BootstrapIndex,'/')
# api.add_resource(douban, '/douban/')
api.add_resource(VueIndex, '/vue/')