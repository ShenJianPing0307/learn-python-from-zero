from flask import Flask, render_template, make_response

app = Flask(__name__)


@app.route('/index')
def index():
    response = make_response(render_template('index.html', num=56))
    response.headers['X-Parachutes'] = 'parachutes are cool'
    response.set_cookie("userinfo", "zhangsan,123456")
    return response


if __name__ == '__main__':
    app.run()