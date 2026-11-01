import json
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8000


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send(self, status, body, content_type="text/plain"):
        data = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/":
            self._send(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send(200, json.dumps(data), "application/json")
        elif self.path == "/status":
            self._send(200, "OK")
        else:
            self._send(404, "404 Not Found - Endpoint not found")


if __name__ == "__main__":
    server = HTTPServer(("localhost", PORT), SimpleAPIHandler)
    print(f"Server running at http://localhost:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()