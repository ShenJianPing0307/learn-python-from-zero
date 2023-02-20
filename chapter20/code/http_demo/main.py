import http.server
import socketserver

users = [
    {"nickname": '我是一只小蜜蜂'},
]
content = """
%s:%s
""" % (users[0].keys(), users[0].values())

with open('index.html', mode='w') as f:
    f.write(content)

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port:", PORT)
    httpd.serve_forever()
