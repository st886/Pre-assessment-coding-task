from http.server import BaseHTTPRequestHandler, HTTPServer


# Define a simple HTTP request handler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the html message
        with open('Variant2.html', 'rb') as file:
            self.wfile.write(file.read())

# Set the server address and port
server_address = ('', 8000)

# Create HTTP server
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

# Print a message indicating the server is running
print("Serving at port 8000")

# Start the server
httpd.serve_forever()