import flask
from flask import Flask
from flask import request

app=Flask(__name__,
          static_url_path='/static',#静态文件路径
          static_folder='static',

          template_folder='templates'#模板文件(前端代码)
          )


####Flask传参方式
# ##<1>‘/’传参
# @app.route('/a/<user_id>/<int:user_pwd>')
# def a(user_id,user_pwd):
#     return "I'm a:%s===%s."%(user_id,user_pwd)
#     pass
#
# ##<2.1>'GET'传参
# @app.route('/a',methods=['GET'])
# def a():
#     user_name=request.args.get('uname')
#     user_pwd=request.args.get('upwd')
#     return "I'm a:%s---%s."%(user_name,user_pwd)
#     pass
# ##<2.2>'POST'传参
# @app.route('/a',methods=['POST'])
# def a():
#     user_name=request.form.get('uname')
#     user_pwd=request.form.get('upwd')
#     return "I'm a:%s---%s."%(user_name,user_pwd)
#     pass

#装饰器，关联路由
@app.route('/')
def index():
    return "haha"
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)