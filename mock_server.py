from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

# Use environment variable for server IP/host, defaulting to localhost/placeholder for security
SERVER_HOST = os.getenv("PERIDOT_SERVER_HOST", "YOUR_IP_HERE")
SERVER_PORT = int(os.getenv("PERIDOT_SERVER_PORT", 8000))

class OAuthMockHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"[GET Request] {self.path}")
        if "/ap/oa" in self.path:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            redirect_url = f"http://{SERVER_HOST}:{SERVER_PORT}/auth/o2/token?code=mock_code"
            response = {"status": "success", "redirect": redirect_url}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        print(f"[POST Request] {self.path}")
        if "/auth/o2/token" in self.path:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            response = {
                "access_token": "mock_access_token_peridot_revival",
                "refresh_token": "mock_refresh_token",
                "token_type": "bearer",
                "expires_in": 3600
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server_address = ('0.0.0.0', SERVER_PORT)
    HTTPServer.allow_reuse_address = True
    httpd = HTTPServer(server_address, OAuthMockHandler)
    print(f"Mock auth server running on port {SERVER_PORT}...")
    httpd.serve_forever()
