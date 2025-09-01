import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import database
from decimal import Decimal

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)

class ApiRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        print(parsed_path)
        if parsed_path.path == '/properties':
            filters_raw = parse_qs(parsed_path.query)
            filters = {k: v[0] for k, v in filters_raw.items()}

            properties = database.get_properties(filters)

            if properties is not None:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()

                json_response = json.dumps(properties, cls=CustomJSONEncoder)
                self.wfile.write(json_response.encode('utf-8'))

            else:
                self.send_response(500, "Internal Server Error")
        else:
            self.send_response(404, "Route Not Found")