## 一、什么是Web编程

socket编程是基于TCP/UDP协议，应用程序比如是QQ等，而目前使用比较多的是浏览器应用程序，主要是基于HTTP协议，所以Web编程可以说是基于HTTP协议的编程。那么基于HTTP协议的话必须符合HTTP协议的要求。

客户端与服务端之间的交互是建立在HTTP协议的基础之上的，它们之间交互的数据信息被称为报文。报文大致被分为报文首部和主体两部分，但不一定非要有报文主体，它们之间以回车符和换行符分割，客户端请求的数据被称为请求报文，服务端返回的数据被成文响应报文。

![](addr-images/1137363-20190930150520419-600298943.png)

### （一）请求报文

![](addr-images/1137363-20190930150554017-592933714.png)

```python
GET /index.html HTTP/1.1 #请求行
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3 #各种首部字段
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
#空行 （CR+LF）...
```

可以看到请求行和各种首部字段（HTTP首部字段）都属于报文首部内容。

#### 1、请求行

请求行由请求方法、Request-URI、HTTP协议版本构成。

- 请求方法

| **方法**    | **说明**                                             | **支持的****HTTP****协议版本** |
| ----------- | ---------------------------------------------------- | ------------------------------ |
| **GET**     | 请求获取Request-URI所标识的资源                      | 1.0、1.1                       |
| **POST**    | 在Request-URI所标识的资源后附加新的数据              | 1.0、1.1                       |
| **PUT**     | 请求服务器存储一个资源，并用Request-URI作为其标识    | 1.0、1.1                       |
| **HEAD**    | 请求获取由Request-URI所标识的资源报文首部            | 1.0、1.1                       |
| **DELETE**  | 请求服务器删除Request-URI所标识的资源                | 1.0、1.1                       |
| **OPTIONS** | 请求查询服务器的性能，或者查询与资源相关的选项和需求 | 1.1                            |
| **TRACE**   | 请求服务器回送收到的请求信息，主要用于测试或诊断     | 1.1                            |
| **CONNECT** | 要求用隧道协议连接代理                               | 1.1                            |

- Request-URI

Request-URI是一个统一资源标识符，标识某一互联网资源（例如/index.html），而常用的 URL 表示资源的地点（互联网上所处的位置），所以URL是URI的子集。

- HTTP协议版本

表示请求的HTTP协议版本, 比如HTTP/1.1，HTTP/1.0。

#### 2、HTTP首部字段

在请求报文中的报文首部包括请求行和HTTP首部字段，HTTP首部字段有通用首部字段、请求首部字段、实体首部字段。这些首部字段的由字段名和字段值构成，字段名和字段值之间以“：”分隔。

- 通用首部字段

请求报文和响应报文都会使用的字段

| **首部字段名**        | **说明**                                         |
| --------------------- | ------------------------------------------------ |
| **Cache-Control**     | 控制缓存的行为                                   |
| **Connection**        | 两个作用：控制不再转发给代理以及管理持久连接     |
| **Date**              | 创建报文的日期时间                               |
| **Pragma**            | 报文指令                                         |
| **Trailer**           | 会事先说明在报文主体后记录了哪些首部字段         |
| **Transfer-Encoding** | 指定报文主体的传输编码方式                       |
| **Upgrade**           | 升级为其他协议                                   |
| **Via**               | 追踪客户端和服务器之间的请求和响应报文的传输路径 |
| **Warning**           | 通常会告知用户一些与缓存相关的问题的警告         |

- 请求首部字段

从客户端向服务端发送请求时使用的首部字段，常见请求首部字段：

| **首部字段名**        | **说明**                                                     |
| --------------------- | ------------------------------------------------------------ |
| **Accept**            | 浏览器可接受的MIME类型                                       |
| **Accept-Charset**    | 浏览器可接受的字符集。                                       |
| **Accept-Encoding**   | 浏览器能够进行解码的数据编码方式。                           |
| **Accept-Language**   | 浏览器所希望的语言种类。                                     |
| **Authorization**     | Web认证信息，通常出现在对服务器发送的WWW-Authenticate头的应答中 |
| **Host**              | 请求资源所在服务器                                           |
| **Content-Length**    | 表示请求消息正文的长度。                                     |
| **If-Modified-Since** | 客户端通过这个首部告诉服务器，资源的缓存时间                 |
| **Referer**           | 客户端通过这个首部告诉服务器，它是从哪个资源来访问服务器的(防盗链)。包含一个URL，用户从该URL代表的页面出发访问当前请求的页面。 |
| **User-Agent**        | User-Agent头域的内容包含发出请求的用户信息，浏览器类型。     |
| **From**              | 请求发送者的email地址，由一些特殊的Web客户程序使用，浏览器不会用到它。 |
| **Range**             | 实体的字节范围请求                                           |

-  实体首部字段

针对请求实体规定的首部字段，对于请求方式是GET的话就没有请求实体，如果是POST等请求方式是有请求实体的。所以在请求和响应报文中都有可能包含实体部分，也就是说可能包含下面这些首部：

| **首部字段名**       | **说明**                                                     |
| -------------------- | ------------------------------------------------------------ |
| **Allow**            | 服务端资源可支持的HTTP方法                                   |
| **Content-Encoding** | 实体主体适用的编码方式                                       |
| **Content-Language** | 告诉客户端实体主体的自然语言                                 |
| **Accept-Language**  | 浏览器所希望的语言种类。                                     |
| **Content-Length**   | 实体主体的大小（单位：字节）                                 |
| **Content-Location** | 报文主体返回对应资源的URI                                    |
| **Content-MD5**      | 由一串由MD5算法生成的值，其目的在于检查报文 主体在传输中是否保持完整，以及确认传输到达。 |
| **Content-Range**    | 实体主体的位置范围                                           |
| **Content-Type**     | 实体主体的媒体类型                                           |
| **Expires**          | 实体主体过期的日期时间                                       |
| **Last-Modified**    | 资源的最后修改日期时间                                       |

### （二）响应报文

响应报文顾名思义就是服务端返回给客户端的数据信息。

![img](https://img2018.cnblogs.com/blog/1137363/201909/1137363-20190930172502723-510144631.png)

上面就是响应报文的结构形式，具体响应报文类似以下的内容：

```
HTTP/1.1 200 0k#状态行
Content-Length: 865    #HTTP首部字段
Content-Type: text/html; charset=utf-8
Date: Mon, 30 Sep 2019 03:00:13 GMT
Server: WSGIServer/0.2 CPython/3.5.2
X-Frame-Options: SAMEORIGIN
#空行######################
<html lang="en">   #报文主体
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="/static/bootstrap-3.3.7-dist/css/bootstrap.css"/>
</head>
<body>
...
...
</body>
</html>
```

状态行和HTTP首部字段属于响应报文的报文首部内容。

#### 1、状态行

包含表明响应结果的状态码，原因短语和 HTTP 版本。

- 状态码

当客户端发送请求后，依照服务端返回的状态码来确定请求处理的情况。

 状态码分为5类：

| **状态类别** | **说明**                                 |
| ------------ | ---------------------------------------- |
| **1xx**      | 指示信息，表示请求已接收，继续处理       |
| **2XX**      | 成功，表示请求已被成功接收、理解、接受   |
| **3xx**      | 重定向，要完成请求必须进行更进一步的操作 |
| **4xx**      | 客户端错误，请求有语法错误或请求无法实现 |
| **5xx**      | 服务器端错误，服务器未能实现合法的请求   |

以下状态码是常用的：

| **类别说明**          | **状态码**          | **原因短语**                                                 | **说明**                                                     |
| --------------------- | ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **2xx****成功**       | 200                 | Ok                                                           | 请求已正常处理                                               |
| 204                   | No Content          | 请求处理成功，但没有任何资源可以返回给客户端                 |                                                              |
| **3xx****重定向**     | 301                 | Moved Permanently                                            | 请求的资源已经被分配了新的URI，以后应使用资源现在所指的URI。 |
| 302                   | Found               | 和301相似，但302代表的资源不是永久性移动，只是临时性的，以后还可能变。 |                                                              |
| 303                   | See Other           | 资源的URI已更新，临时按新的URI以GET方式请求资源              |                                                              |
| 304                   | Not Modified        | 资源已找到，但未符合请求的条件，返回304                      |                                                              |
| 307                   | Temporary Redirect  | 临时重定向。与302有相同的含义。                              |                                                              |
| **4xx****客户端错误** | 400                 | Bad Request                                                  | 服务器端无法理解客户端发送的请求，请求报文中可能存在语法错误。 |
| 401                   | Unauthorized        | 发送的请求需要有通过HTTP认证（BASIC认证，DIGEST认证）的认证信息 |                                                              |
| 403                   | Forbidden           | 不允许访问那个资源。该状态码表明对请求资源的访问被服务器拒绝了（例如无权限，未授权等）。 |                                                              |
| 404                   | Not Found           | 服务器上没有请求的资源，也有可能是请求路劲错误。             |                                                              |
| **5xx****服务器错误** | 500                 | Internal Server Error                                        | 该状态码表明服务器端在执行请求时发生了错误。也有可能是 Web应用存在的 bug 或某些临时的故障。 |
| 503                   | Service Unavailable | 服务器正在忙碌。该状态码表明服务器暂时处于超负载或正在停机维护，现在无法处理请求。 |                                                              |

- 原因短语

原因短语在上述状态码中已经说明

- HTTP协议版本

表示响应的HTTP协议版本, 比如HTTP/1.1，HTTP/1.0，与请求报文请求行中的一样。

#### 2、HTTP首部字段

在响应报文的响应首部中，状态行后就是HTTP首部字段，它与请求报文的请求首部中的HTTP首部字段不同之处在于将请求首部字段变成了响应首部字段。

- 通用首部字段

参考请求报文中的通用首部字段

- 响应首部字段

| **首部字段名**         | **说明**                                                     |
| ---------------------- | ------------------------------------------------------------ |
| **Accept-Ranges**      | 告知客户端，服务器是否接受字节范围请求                       |
| **Age**                | 告知客户端，服务器资源创建经过的时间                         |
| **ETag**               | 告知客户端资源的实体标识。它是一种可以将资源以字符串形式做唯一性标识的方式。服务器会为每份资源分配对应的ETag。 |
| **Location**           | 令客户端重定向至指定URI                                      |
| **Proxy-Authenticate** | 代理服务器对客户端的认证信息                                 |
| **Retry-After**        | 告知客户端应该在多久之后再次发送请求                         |
| **Server**             | 告知客户端当前服务器上安装的HTTP服务器应用程序的信息         |
| **Vary**               | 该首部字段可对缓存进行控制。源服务器会向代理服务器传达关于本地缓存使用方法的命令 |
| **WWW-Authenticate**   | 服务器对客户端的认证信息，它会告知客户端适用于访问请求URI所指定资源的认证方案（Basic还是Digest）和带参数提示的质询。状态码401 Unauthorized响应中，要使用该首部字段。 |

- 实体首部字段

参考请求报文中的实体首部字段

## 二、HTTP报文补充

### （一）报文主体与报文实体

#### 1、报文 

是HTTP通信中的基本单位，站点一次性要发送的数据块，通过HTTP通信传输。

#### 2、报文实体

作为请求或响应的有效载荷数据（补充项）被传输，其内容由实体首部和实体主体组成。

#### 3、报文主体

用于传输请求或响应的实体主体。

#### 4、报文主体与报文实体

通常报文主体等同于报文实体，只有当传输中进行编码操作时，实体主体的内容发生变化，才导致它和报文主体产生差异。

如下图所示：

![](addr-images/1137363-20190930183011341-754910775.png)

### （二）HTTP首部

HTTP报文整体分为报文首部与报文主体两部分，中间以空行分隔，无论是请求报文还是响应报文，它们的首部包含请求行（响应行）与HTTP首部。

HTTP首部中除了通用首部字段、请求首部字段、响应首部字段、实体首部字段外还有其它的一些字段。

#### 1、为cookie服务的首部字段

| **首部字段名** | **说明**                                                     |
| -------------- | ------------------------------------------------------------ |
| **Set-Cookie** | 响应首部字段，Cookie 会根据从服务器端发送的响应报文内的一个叫做 Set-Cookie 的首部字段信息，通知客户端保存 Cookie |
| **Cookie**     | 请求首部字段，服务器端会从请求报文中去发现Cookie这个首部字段信息，然后与服务器上的记录做对比检查，得到之前的状态信息 |

####  2、其它

- X-XSS-Protection

首部字段 X-XSS-Protection 属于 HTTP 响应首部，它是针对跨站脚本攻击（XSS）的一种对策，用于控制浏览器 XSS 防护机制的开关。

```
X-XSS-Protection：0 #将 XSS 过滤设置成无效状态
X-XSS-Protection：1 #将 XSS 过滤设置成有效状态X-XSS-Protection：1;mode=block #表示启用XSS过滤器X-XSS-Protection：1;report=<reporting-uri> #表示启用 XSS 过滤
```

- DNT

首部字段 DNT 属于 HTTP 请求首部，其中 DNT 是 Do Not Track 的简称，意为拒绝个人信息被收集，用户选择了这个字段就可以免于被第三方网站追踪网络痕迹。

```
DNT：0 #同意被追踪
DNT：1 #拒绝被追踪
```

## 三、一个简单的HTTP服务器

```python
import socket

sk = socket.socket()

sk.bind(("127.0.0.1", 9600))

sk.listen()

while True:
    # 等待连接
    conn, addr = sk.accept()
    # 接收数据
    data = conn.recv(1024)
    # 返回状态行
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    # 返回体
    conn.send(b"world")
    # 关闭连接
    conn.close()

```

通过 http://127.0.0.1:9600/进行访问

## 四、Web框架初步演化

### （一）模板

```python
import socket

sk = socket.socket()

sk.bind(("127.0.0.1", 9600))

sk.listen()

while True:
    # 等待连接
    conn, addr = sk.accept()
    # 接收数据
    data = conn.recv(1024)
    # 返回状态行
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    # 返回体，读取文件内容
    with open("index.html", mode="rb") as f:
        res = f.read()
    conn.send(res)
    # 关闭连接
    conn.close()

```

### （二）模板、路由、视图

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 9600))
sock.listen()


def index():
    return b"index"


def home():
    return b"home"


urlpattern = [
    ("/index", index),
    ("/home", home)
]

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    data = str(data, encoding="utf8")
    url = data.split("\r\n")[0].split()[1]
    print(url)
    func = None
    for path_tuple in urlpattern:
        if path_tuple[0] == url:
            func = path_tuple[1]
            break
    if func:
        response = func()
    else:
        response = b"404 not found!"
    # 返回响应状态行
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n")
    # 返回响应体
    conn.send(response)
    conn.close()

```

### （三）服务器程序与应用程序

web框架本质就是一个socket服务端。

web框架功能：

- socket收发消息
- 根据不同的路径返回不同的内容
- 可以返回页面

对于真实开发中的python web程序来说，一般会分为两部分：服务器程序和应用程序。

服务器程序负责对socket服务器进行封装，并在请求到来时，对请求的各种数据进行整理。

应用程序则负责具体的逻辑处理。为了方便应用程序的开发，就出现了众多的Web框架，例如：Django、Flask、web.py 等。不同的框架有不同的开发方式，但是无论如何，开发出的应用程序都要和服务器程序配合，才能为用户提供服务。

这样，服务器程序就需要为不同的框架提供不同的支持。这样混乱的局面无论对于服务器还是框架，都是不好的。对服务器来说，需要支持各种不同框架，对框架来说，只有支持它的服务器才能被开发出的应用使用。

这时候，标准化就变得尤为重要。我们可以设立一个标准，只要服务器程序支持这个标准，框架也支持这个标准，那么他们就可以配合使用。一旦标准确定，双方各自实现。这样，服务器可以支持更多支持标准的框架，框架也可以使用更多支持标准的服务器。

WSGI（Web Server Gateway Interface）就是一种规范，它定义了使用Python编写的web应用程序与web服务器程序之间的接口格式，实现web应用程序与web服务器程序间的解耦。

那么WSGI定义的究竟是一种什么样的规范呢？

- 应用程序/框架
- 服务器/网关

#### 1、应用程序/框架

应用程序对象是一个接受两个参数的可调用对象。函数、方法、类或带有`__call__`方法的实例都可以用作应用程序对象。应用程序对象必须能够被多次调用，因为几乎所有服务器/网关（CGI 除外）都会发出此类重复请求。

这是两个示例应用程序对象；一个是函数，另一个是类：

```python
def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world!\n']


class AppClass:
    """Produce the same output, but using a class

    (Note: 'AppClass' is the "application" here, so calling it
    returns an instance of 'AppClass', which is then the iterable
    return value of the "application callable" as required by
    the spec.

    If we wanted to use *instances* of 'AppClass' as application
    objects instead, we would have to implement a '__call__'
    method, which would be invoked to execute the application,
    and we would need to create an instance for use by the
    server or gateway.
    """

    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain')]
        self.start(status, response_headers)
        yield "Hello world!\n"
```

#### 2、服务器/网关

服务器或网关针对它从 HTTP 客户端接收到的每个针对应用程序的请求调用一次可调用应用程序。为了说明这一点，这里有一个简单的 CGI 网关，实现为采用应用程序对象的函数。如果服务器中触发可调用应用程序，就是可符合WSGI协议的WSGI服务器。

```python
import os, sys

def run_with_cgi(application):

    environ = dict(os.environ.items())
    environ['wsgi.input']        = sys.stdin
    environ['wsgi.errors']       = sys.stderr
    environ['wsgi.version']      = (1, 0)
    environ['wsgi.multithread']  = False
    environ['wsgi.multiprocess'] = True
    environ['wsgi.run_once']     = True

    if environ.get('HTTPS', 'off') in ('on', '1'):
        environ['wsgi.url_scheme'] = 'https'
    else:
        environ['wsgi.url_scheme'] = 'http'

    headers_set = []
    headers_sent = []

    def write(data):
        if not headers_set:
             raise AssertionError("write() before start_response()")

        elif not headers_sent:
             # Before the first output, send the stored headers
             status, response_headers = headers_sent[:] = headers_set
             sys.stdout.write('Status: %s\r\n' % status)
             for header in response_headers:
                 sys.stdout.write('%s: %s\r\n' % header)
             sys.stdout.write('\r\n')

        sys.stdout.write(data)
        sys.stdout.flush()

    def start_response(status, response_headers, exc_info=None):
        if exc_info:
            try:
                if headers_sent:
                    # Re-raise original exception if headers sent
                    raise exc_info[0], exc_info[1], exc_info[2]
            finally:
                exc_info = None     # avoid dangling circular ref
        elif headers_set:
            raise AssertionError("Headers already set!")

        headers_set[:] = [status, response_headers]
        return write

    result = application(environ, start_response) # 触发应用程序
    try:
        for data in result:
            if data:    # don't send headers until body appears
                write(data)
        if not headers_sent:
            write('')   # send headers now if body was empty
    finally:
        if hasattr(result, 'close'):
            result.close()
```

可以看到这个是比较复杂的，不过有很多实现的WSGI服务器，常用的WSGI服务器有uwsgi、Gunicorn。而Python标准库提供的独立WSGI服务器叫wsgiref，Django开发环境用的就是这个模块来做服务器。

 符合WSGI协议的服务器会回调start_response方法：

```python
 result = application(environ, start_response) # 触发应用程序
```

 总的来说WSGI协议主要有三点：

- 接受environ 和start_response两个参数
- 内部调用 start_respons生成header
- 返回一个可迭代的响应体

那么可以使用Python内置wsgiref模块来实现web服务器：

```python
from wsgiref.simple_server import make_server


def index():
    return b"index"


def home():
    return b"home"


urlpattern = [
    ("/index", index),
    ("/home", home)
]


def simple_app(environ, start_response):
    status = "200 OK"
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    current_path = environ.get("PATH_INFO")
    func = None
    for path_tuple in urlpattern:
        if path_tuple[0] == current_path:
            func = path_tuple[1]
            break
    if func:
        response = func()
    else:
        response = b"404 not found!"
    return [response, ]


if __name__ == '__main__':
    srv = make_server("127.0.0.1", 9000, simple_app)
    srv.serve_forever()
```

## 五、werkzeug程序库

### （一）什么是werkzeug程序库

上面的应用程序的路由以及请求、相应都是自己完成的，那么怎么解决这个问题呢？

Werkzeug是一个全面的WSGI web应用程序库。它最初是WSGI应用程序的各种实用程序的简单集合，在WSGI的基础上假如很多新的东西：

- 路由处理
- request和response封装
- 自带WSGI Server

本文使用的WerkZeug版本：WerkZeug2.2.2

### （二）request、response封装

Werkzeug是一个用于WSGI的实用程序库。WSGI本身是一种协议或约定，可以确保您的web应用程序可以与web服务器对话，更重要的是，web应用程序可以很好地协同工作。

在没有Werkzeug的帮助下，WSGI中一个基本的“Hello World”应用程序是这样的：

```python
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello World!'.encode('utf-8')]
```

WSGI应用程序并传递一个environ dict和一个start_response可调用对象。环境包含所有传入信息，可以使用start_response函数指示响应的开始。使用Werkzeug，您不必直接处理这两种情况，因为提供了请求和响应对象来处理它们。

请求数据接受环境对象，并允许您以良好的方式访问来自该环境的数据。响应对象本身就是一个WSGI应用程序，它提供了一种更好的方式来创建响应。

你可以这样写：

```python
from werkzeug.wrappers import Response

def application(environ, start_response):
    response = Response('Hello World!', mimetype='text/plain')
    return response(environ, start_response)
```

以下是使用请求、响应对象编写该应用程序的方法，它查看URL中的查询字符串：

```python
from werkzeug.wrappers import Request, Response

def application(environ, start_response):
    request = Request(environ)
    text = f"Hello {request.args.get('name', 'World')}!"
    response = Response(text, mimetype='text/plain')
    return response(environ, start_response)
```

### （三）路由处理

在WerkZeug中有路由处理的部分：

```python
from werkzeug.routing import Map, Rule
```

如下实例：

```python
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.serving import run_simple


def index(request):
    return "index"


def home(request):
    return "home"


# 路由
url_pattern = Map([
    Rule('/index', endpoint='index'),
    Rule('/home', endpoint='home')
])


# 分发路由
def dispatch_request(request):
    adapter = url_pattern.bind_to_environ(request.environ)
    try:
        endpoint, values = adapter.match()
        return eval(endpoint)(request, **values)  # 可以使用反射getattr
    except HTTPException or NotFound as e:
        return e


def application(environ, start_response):
    request = Request(environ)
    text = dispatch_request(request)
    response = Response(text, mimetype='text/plain')
    return response(environ, start_response)


if __name__ == '__main__':
    run_simple('127.0.0.1', 5001, application)

"""
出现异常原因， 当访问/index或者/home默认发送，/favicon.ico请求导致发生异常
"""

```

### （四）实例

#### 1、创建文件夹

在开始之前，创建这个应用程序所需的文件夹:

```python
/manager
    /static
    /templates
```

manager文件夹不是一个python包，而只是我们放置文件的地方。直接进入这个文件夹，然后我们将把我们的主模块直接放到这个文件夹。应用程序的用户可以通过HTTP访问静态文件夹中的文件。这是存放CSS和JavaScript文件的地方。在模板文件夹中，我们将让Jinja2查找模板。

#### 2、基础结构

现在，让我们开始为应用程序创建一个模块。让我们在manager文件夹中创建一个名为main.py的文件。

```python
import os
import redis
from werkzeug.urls import url_parse
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader
```

然后，我们可以为我们的应用程序创建基本结构和一个函数来创建它的新实例，还可以选择使用一个WSGI中间件来导出web上静态文件夹中的所有文件：

```python
class Application:

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, f'on_{endpoint}')(request, **values)
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


if __name__ == '__main__':
    # 加入静态文件，如果不需要直接使用 app = Application() 即可
    app = SharedDataMiddleware(Application(), {'/static': os.path.join(os.path.dirname(__file__), 'static')})
    run_simple('127.0.0.1', 5003, app)

```

这里的基本思想是我们的Application类是一个实际的WSGI应用程序。__call__方法直接分派到wsgi_app。这样我们就可以包装wsgi_app来应用中间件。实际的wsgi_app方法创建一个Request对象并调用dispatch_request方法，该方法必须返回一个Response对象，然后再次作为WSGI应用程序。

创建应用程序的新实例。它不仅将一些参数作为配置传递给应用程序，而且还可选地添加一个导出静态文件的WSGI中间件。这样，即使我们没有配置服务器来提供这些文件，我们也可以从静态文件夹中访问这些文件，这对开发非常有帮助。

#### 3、环境

现在我们有了基本的应用程序类，我们可以让构造函数做一些有用的事情，并在那里提供一些有用的帮助程序。让我们扩展一下类:

```python
    def __init__(self):
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path), 		                                        autoescape=True)


    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')
```

#### 4、路由

接下来是路由。路由是将URL匹配并解析为我们可以使用的内容的过程。Werkzeug提供了一个灵活的集成路由系统，我们可以使用它。它的工作方式是创建一个Map实例并添加一堆Rule对象。每个规则都有一个模式，它将尝试匹配URL和一个“端点”。端点通常是一个字符串，可用于唯一地标识URL。我们也可以使用它来自动反转URL。

把这个放进构造函数:

```python
    def __init__(self):
        self.url_map = Map([
            Rule('/list', endpoint='list'),
            Rule('/detail/<id>', endpoint='detail')
        ])
```

这里使用了两个规则创建一个URL映射。

那么如何从端点找到函数呢?这取决于你。在本教程中，我们将在类本身上调用方法on_ + endpoint。下面是它的工作原理：

```python
    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, f'on_{endpoint}')(request, **values)
        except HTTPException as e:
            return e
```

我们将URL映射绑定到当前环境，返回URLAdapter。适配器可用于匹配请求，也可用于反向url。match方法将返回端点和URL中的值字典。

如果它不匹配任何东西，它将引发NotFound异常，这是一个HTTPException。所有HTTP异常本身也是WSGI应用程序，它们呈现默认错误页面。我们只需要把它们都捕捉下来，然后返回错误本身。 

如果一切正常，我们调用on_ + endpoint函数，并将请求作为参数传递给它，并将所有URL参数作为关键字参数传递给它，并返回方法返回的响应对象。

#### 5、视图

创建两个URL映射的视图函数：

```python
    def on_list(self, request):
        if request.method == 'GET':
            return self.render_template('list.html', data=self.stu_list)

    def on_detail(self, request, id):
        obj = {}
        for stu in self.stu_list:
            if stu.get("id") == int(id):
                obj = stu
        return self.render_template('detail.html', obj=obj)
```

根据不同的请求method获取不同的资源，一般进行业务处理，从数据库中获取数据进行处理，然后返回给页面，这里通过指定的数据模拟数据库中的数据，在构造方法中：

```python
    def __init__(self):
        self.stu_list = [
            {"id": 1, "name": "zhangsan", "age": 15},
            {"id": 2, "name": "lisi", "age": 13},
        ]
```

#### 6、模板

将所有的模板文件放入templates目录中，jinja2支持模板很多操作，如：渲染后台数据、模板继承等。

- list.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="/static/list.css">
</head>
<body>
<div id="title">学生列表</div>
{% for stu in data %}
    <p><a href="/detail/{{ stu.id }}">{{ stu.name }}</a></p>
{% endfor %}
</body>
</html>
```

- detail.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
{% if obj %}
    {{ obj.id }}-{{ obj.name }}-{{ obj.age }}
{% endif %}
</body>
</html>
```

#### 7、样式表

在html模板中，虽然渲染了后台的数据，但是页面样式有所欠缺，此时可以在`static`目录中引入list.css样式表：

```css
body { background: #E8EFF0; margin: 0; padding: 0; }
# title {
    background-color: aqua;
  }
```

然后在模板中引入即可。

#### 8、完整后台代码

```python
from werkzeug.serving import run_simple
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.middleware.shared_data import SharedDataMiddleware
import os
from jinja2 import Environment, FileSystemLoader


class Application:

    def __init__(self):
        self.url_map = Map([
            Rule('/list', endpoint='list'),
            Rule('/detail/<id>', endpoint='detail')
        ])
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)
        self.stu_list = [
            {"id": 1, "name": "zhangsan", "age": 15},
            {"id": 2, "name": "lisi", "age": 13},
        ]

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    def on_list(self, request):
        if request.method == 'GET':
            return self.render_template('list.html', data=self.stu_list)

    def on_detail(self, request, id):
        obj = {}
        for stu in self.stu_list:
            if stu.get("id") == int(id):
                obj = stu
        return self.render_template('detail.html', obj=obj)

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, f'on_{endpoint}')(request, **values)
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


if __name__ == '__main__':
    # 加入静态文件，如果不需要直接使用 app = Application() 即可
    app = SharedDataMiddleware(Application(), {'/static': os.path.join(os.path.dirname(__file__), 'static')})
    run_simple('127.0.0.1', 5003, app)

```









































