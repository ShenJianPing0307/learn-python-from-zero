from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wrappers import Response, Request
from werkzeug.routing import Map, Rule

from werkzeug.serving import run_simple


def index(request):
    return b"index"


def home(request):
    return b"home"


url_pattern = Map([
    Rule('/index', endpoint='index'),
    Rule('/home', endpoint='home')
])


# 分发地址
def dispatch_request(request):
    adapter = url_pattern.bind_to_environ(request.environ)
    try:
        endpoint, values = adapter.match()
        return eval(endpoint)(request, **values)  # index(request)
    except HTTPException or NotFound as e:
        return e


def application(environ, start_response):
    request = Request(environ)
    text = dispatch_request(request)
    response = Response(text)
    return response(environ, start_response)


if __name__ == '__main__':
    run_simple("127.0.0.1", 9005, application)
