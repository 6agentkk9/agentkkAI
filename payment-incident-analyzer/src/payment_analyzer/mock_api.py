"""Tiny local mock gateway API for learning and manual testing."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


PAYMENTS = {
    "PAY-10001": {
        "payment_id": "PAY-10001",
        "status": "DECLINED",
        "response_code": "51",
        "message": "Insufficient funds",
    },
    "PAY-10002": {
        "payment_id": "PAY-10002",
        "status": "PENDING",
        "response_code": "TIMEOUT",
        "message": "Gateway response is pending investigation",
    },
    "PAY-10003": {
        "payment_id": "PAY-10003",
        "status": "FAILED",
        "response_code": "96",
        "message": "System malfunction",
    },
}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        payment_id = self.path.rstrip("/").split("/")[-1]
        payload = PAYMENTS.get(payment_id)
        if payload is None:
            self.send_response(404)
            payload = {"error": "Payment not found"}
        else:
            self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode("utf-8"))

    def log_message(self, format, *args):
        # Keep the mock server output concise.
        print(format % args)


def main():
    server = HTTPServer(("127.0.0.1", 8000), Handler)
    print("Mock payment API listening at http://localhost:8000")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping mock API.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
