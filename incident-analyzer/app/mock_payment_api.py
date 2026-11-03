from http.server import BaseHTTPRequestHandler, HTTPServer
import json


PAYMENTS = {
    "PAY-10001": {
        "payment_id": "PAY-10001",
        "gateway": "MockGateway",
        "gateway_status": "DECLINED",
        "response_code": "51",
        "response_message": "Insufficient funds"
    },
    "PAY-10002": {
        "payment_id": "PAY-10002",
        "gateway": "MockGateway",
        "gateway_status": "TIMEOUT",
        "response_code": "TO",
        "response_message": "Gateway request timed out"
    },
    "PAY-10003": {
        "payment_id": "PAY-10003",
        "gateway": "MockGateway",
        "gateway_status": "FAILED",
        "response_code": "G01",
        "response_message": "Gateway processing error"
    },
    "PAY-10004": {
        "payment_id": "PAY-10004",
        "gateway": "MockGateway",
        "gateway_status": "DECLINED",
        "response_code": "05",
        "response_message": "Do not honor",
        "amount": "1250.75",
        "currency": "USD"
    }  
}


class PaymentApiHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        payment_id = self.path.split("/")[-1]

        payment = PAYMENTS.get(payment_id)

        if payment is None:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Payment not found")
            return

        response = json.dumps(payment).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(response)


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), PaymentApiHandler)

    print("Mock Payment API running on http://localhost:8000")

    server.serve_forever()