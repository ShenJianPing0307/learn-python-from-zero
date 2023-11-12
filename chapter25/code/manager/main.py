import os
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException
from werkzeug.middleware.shared_data import SharedDataMiddleware
from jinja2 import Environment, FileSystemLoader
from werkzeug.serving import run_simple


class Application:

    def __init__(self):
        template_path = os.path.join(os.path.dirname(__file__), "template")
        self.jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)
        self.url_map = Map([
            Rule('/add', endpoint='add'),
            Rule('/list', endpoint='list'),
            Rule('/detail/<id>', endpoint='detail')
        ])
        self.stu_list = [
            {"id": 1, "name": "zhangsan", "age": 15},
            {"id": 2, "name": "lisi", "age": 13},
        ]
    def on_add(self, request):
        if request.method == 'GET':
            return self.render_template('add.html')
        elif request.method == 'POST':
            id = request.form.get('id')
            name = request.form.get('name')
            age = request.form.get('age')
            self.stu_list.append({'id':id, 'name':name, 'age':age})
            return self.render_template('list.html', data=self.stu_list)

    def on_list(self, request):
        if request.method == 'GET':
            return self.render_template('list.html', data=self.stu_list)

    def on_detail(self, request, id):
        obj = {}
        for stu in self.stu_list:
            if stu.get("id") == int(id):
                obj = stu
        return self.render_template("detail.html", obj=obj)

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, f'on_{endpoint}')(request, **values)
        except HTTPException as e:
            return e

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype="text/html")

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


if __name__ == '__main__':
    app = SharedDataMiddleware(Application(), {'/static': os.path.join(os.path.dirname(__file__), 'static')})
    run_simple('127.0.0.1', 5003, app)


