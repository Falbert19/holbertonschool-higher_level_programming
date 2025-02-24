#!/usr/bin/python3
"""
task_03_http_server.py

A simple API built using Python's http.server module.

This server supports multiple endpoints:
- GET /         : Returns a plain text greeting.
- GET /data     : Returns sample JSON data.
- GET /status   : Returns a plain text status ("OK").
- GET /info     : Returns API information in JSON format.

For any undefined endpoint, a 404 Not Found error is returned.
"""
import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Handle GET requests and route them
        based on the URL path.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0", "description":
                "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode())

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")



if __name__ == "__main__":
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Starting server on port 8000...")
    httpd.serve_forever()
