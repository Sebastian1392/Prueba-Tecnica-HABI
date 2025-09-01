from http.server import HTTPServer
from api_handler import ApiRequestHandler

PORT = 8000

if __name__ == '__main__':
    server = HTTPServer(('', PORT), ApiRequestHandler)
    print(f"Started server in http://localhost:{PORT}")
    server.serve_forever()