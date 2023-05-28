from wsgiref.simple_server import make_server


# 视图函数，主要做业务
def index():
    return b"index"


def home():
    return b"home"


# 路由
urlpattern = [
    ("/index.html", index),
    ("/home.html", home)
]


def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
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
        response = b"404 not found..."
    return [response, ]


if __name__ == '__main__':
    server = make_server("127.0.0.1", 9000, simple_app)
    server.serve_forever()
