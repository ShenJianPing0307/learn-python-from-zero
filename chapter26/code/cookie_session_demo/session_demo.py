from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = 'md_hgh58jk'  # 使用session前需要设置该选项，用于对返回前台的cookie进行加密


@app.route('/login')
def login():
    # 登录成功，设置sesion，保存用户信息
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect('/index')
    return render_template('index.html')