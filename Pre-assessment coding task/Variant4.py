from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Define a simple HTTP request handler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/grid-data':
            # Send response status code
            self.send_response(200)
            # Send headers
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # Define grid data
            grid_data = [[i * j for j in range(1, 13)] for i in range(1, 13)]
            # Send the json data
            self.wfile.write(json.dumps(grid_data).encode())

# Set the server address and port
server_address = ('', 8000)

# Create HTTP server
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

# Print a message indicating the server is running
print("Serving at port 8000")

# Start the server
httpd.serve_forever()