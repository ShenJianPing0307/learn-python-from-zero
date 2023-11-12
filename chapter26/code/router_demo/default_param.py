from flask import Flask


app = Flask(__name__)

@app.route('/index',endpoint='index',defaults={'id':10})
def index(id):
    print(id)  #接收传递的默认参数
    return 'index'

if __name__ == '__main__':
    app.run()