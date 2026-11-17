from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, Secure World!")

server = HTTPServer(("0.0.0.0", 8080), Handler)
server.serve_forever()