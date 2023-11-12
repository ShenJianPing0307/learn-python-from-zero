## 一、什么是Flask

- Web框架

> flask（小而精）、Django（大而全）、FastAPI（异步 性能高）

[官网](https://flask.palletsprojects.com/en/2.3.x/)

Flask 依赖于[Werkzeug](https://werkzeug.palletsprojects.com/) WSGI 工具包、[Jinja](https://jinja.palletsprojects.com/)模板引擎和 [Click](https://click.palletsprojects.com/) CLI 工具包。

### （一）认识Flask

```python
pip install flask
```

```python
from flask import Flask

app = Flask(__name__)


@app.route("/index")
def index():
    return "index"


if __name__ == '__main__':
    app.run()

```

### （二）快速入门

- 后端

```python
from flask import Flask, render_template

app = Flask(__name__)

stu_list = [
    {"id": 1, "name": "zhangsan", "age": 15},
    {"id": 2, "name": "lisi", "age": 13},
]


@app.route("/list")
def list():
    return render_template("list.html", data=stu_list)

if __name__ == '__main__':
    app.run()
```

- 前端

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href=".././static/bootstrap.min.css">
</head>
<body>
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">id</th>
      <th scope="col">name</th>
      <th scope="col">age</th>
    </tr>
  </thead>
  <tbody>
    {% for row in data %}
        <tr>
            <th scope="row">{{ row.id }}</th>
            <td>{{ row.id }}</td>
            <td>{{ row.name }}</td>
            <td>{{ row.age }}</td>
        </tr>
    {% endfor %}
  </tbody>
</table>
<script src=".././static/bootstrap.min.js"></script>
</body>
</html>
```

## 二、组成

- 配置文件
- 路由系统
- 模板系统
- 请求响应

### （一）配置

- 直接配置
- from_pyfile
- from_object

```python
ENV #应用运行于什么环境，在生产环境中不要使用 development 。缺省值： 'production'
DEBUG #是否开启调试模式，在生产环境中不要开启调试模式。缺省值：当 ENV 是 'development' 时，为 True ；否则为 False 。
TESTING #开启测试模式。缺省值： False
PROPAGATE_EXCEPTIONS #当异常发生时，不要弹出请求情境。缺省值： None
TRAP_HTTP_EXCEPTIONS #如果没有处理 HTTPException 类型异常的处理器，重新引发该异常用于被 交互调试器处理，　　　　　　　　　　　　　　而不是作为一个简单的错误响应来返回。缺省值： False
TRAP_BAD_REQUEST_ERRORS #尝试操作一个请求字典中不存在的键，如 args 和 form ，会返回一个 　　　　　　　　　　　　　　400 Bad Request error 页面。缺省值： None
SECRET_KEY #密钥用于会话 cookie 的安全签名，并可用于应用或者扩展的其他安全需求。缺省值： None
SESSION_COOKIE_NAME #会话 cookie 的名称。假如已存在同名 cookie ，本变量可改变。缺省值： 'session'
SESSION_COOKIE_DOMAIN #认可会话 cookie 的域的匹配规则。缺省值： None
SESSION_COOKIE_PATH #认可会话 cookie 的路径。缺省值： None
SESSION_COOKIE_HTTPONLY #为了安全，浏览器不会允许 JavaScript 操作标记为“ HTTP only ”的 cookie 。缺省值： True
SESSION_COOKIE_SECURE #如果 cookie 标记为“ secure ”，那么浏览器只会使用基于 HTTPS 的请求发 送 cookie 。缺省值： False
SESSION_COOKIE_SAMESITE #限制来自外部站点的请求如何发送 cookie 。缺省值： None
PERMANENT_SESSION_LIFETIME #如果 session.permanent 为真， cookie 的有效期为本变量设置的数字， 单位为秒。　　　　　　　　　　　　　　　　　缺省值： timedelta(days=31) （ 2678400 秒）
SESSION_REFRESH_EACH_REQUEST #当 session.permanent 为真时，控制是否每个响应都发送 cookie 。缺省值： True
SERVER_NAME #通知应用其所绑定的主机和端口。子域路由匹配需要本变量。缺省值： None
APPLICATION_ROOT #通知应用应用的根路径是什么。缺省值： '/'
```

#### 1、直接配置

```python
...
app = Flask(__name__)

# 直接配置
app.config['DEBUG'] = True # 调试模式
app.config['SECRET_KEY'] = "ABCDEFG"
...
```

#### 2、文件配置

```python
...
app.config.from_pyfile("config_file/base_config.py")
...
```

#### 3、对象配置

```python
...
# 类的路径
app.config.from_object("config_file.object_base_config.ProConfig")
...
```

### （二）路由系统

- 路由本质

```python
from flask import Flask

app = Flask(__name__)


def index():
    return ""


app.add_url_rule('/index', view_func=index, methods=['GET', 'POST'], endpoint='index')

if __name__ == '__main__':
    app.run()

```

- add_url_rule参数

```python
rule #url规则
view_func #视图名称
defaults = None #缺省值为None，当URL中无参数，函数需要参数时，使用defaults={'k':'v'}为函数提供参数
endpoint = None #缺省值为None，用于反向生成URL，即： url_for('名称')
methods=None #缺省值为None，允许的请求方式，如：["GET","POST"]
redirect_to=None #缺省值为None，重定向到指定地址
strict_slashes=None #缺省值为None，对URL最后的 / 符号是否严格要求
```

- defaults

- redirect_to
- strict_slashes
- 正则

### （三）视图函数

- FBV （function）

```python
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath
```

- CBV    (class)

### （四）模板系统

模板的基础方法：

Flask使用的是Jinja2模板，与模板相关联的方法有：

- render_template
- Markup
- jsonify
- make_response
- macro 

### （五）请求响应

#### 1、请求

```python
from flask import request
```

参数：

```python
"""
request.data
request.form
request.query_string
request.method
request.args
request.values
request.cookies
request.headers
request.path
request.full_path
request.script_root
request.url
request.base_url
request.url_root
request.host_url
request.host
request.files
...
"""
```

源码：

```python
from werkzeug.wrappers import request
```

#### 2、响应

```python
from flask import redirect
from flask import render_template
from flask import make_response
```

- 源码

```python
from werkzeug.wrappers import response
```

## 三、Cookie && Session

HTTP无状态协议

如何保存用户信息，避免重复登录

## 四、请求扩展

类似中间件















