from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = 'md_hgh58jk'  # 使用session前需要设置该选项，用于对返回前台的cookie进行加密


@app.before_request
def process_request(*args, **kwargs):
    if request.path == '/login':
        return None  # 这个请求放行 白名单
    else:
        username = session.get("username")
        if username:
            return None  # 放行
        else:
            return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # 登录成功，设置sesion，保存用户信息
    if request.method == 'POST':
        # session['username'] = request.form['username']
        # session['password'] = request.form['password']
        session['username'] = "zhangsan"
        session['password'] = "123456"
        return redirect('/index')
    return render_template('login.html')


@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
