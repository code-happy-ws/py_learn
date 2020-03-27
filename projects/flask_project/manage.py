from flask import Flask, request,render_template,make_response,Response
from flask_restful import Api
from datetime import datetime
from apps.douban.views import douban
from apps.bootstrap.views import BootstrapIndex

app = Flask(__name__)
api = Api(app)

api.add_resource(BootstrapIndex,'/')
api.add_resource(douban, '/douban/')

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        print(request.method)
        res=Response(render_template('login.html'))
        ex=datetime(year=2020,month=1,day=1,hour=0,minute=0,second=0)
        res.set_cookie('username','zzw',expires=ex,max_age=10)
        res.delete_cookie()
        return res
    else:
        print(request.method)
        username=request.form.get('username')
        password=request.form.get('password')
        repeatpasswd = request.form.get('repeatpasswd')
        print(username,password,repeatpasswd)
        return 'success'

if __name__ == '__main__':
    app.run()
