from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import socket
import time
import os


class SREStatusHandler(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self._send_json({
                "service": "sre-status-service",
                "message": "OK",
                "hostname": socket.gethostname(),
                "time": time.time()
            })
        elif self.path == "/health":
            # Simple health endpoint
            self._send_json({"status": "healthy"})
        elif self.path == "/ready":
            # Simple readiness endpoint
            self._send_json({"status": "ready"})
        else:
            self._send_json({"error": "not found"}, status=404)


def run():
    port = int(os.getenv("PORT", "8000"))
    server = HTTPServer(("", port), SREStatusHandler)
    print(f"[INFO] SRE Status Service listening on port {port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    run()
