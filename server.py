# Import the built-in HTTP server and socket server modules
import http.server
import socketserver

# The port where the server will listen for requests
PORT = 8000

# The directory containing your HTML files
DIRECTORY = "public"

# Define a custom request handler by extending SimpleHTTPRequestHandler
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    # Customize the constructor to use a specific directory for serving files
    def __init__(self, *args, **kwargs):
        # Set the directory where files are served from (like 'public/')
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    # Override the method that handles error responses
    def send_error(self, code, message=None, explain=None):
        # If the error is a 404 (file not found)
        if code == 404:
            # Serve the custom 404.html file instead of the default error page
            self.path = '/404.html'
            self.send_response(404)              # Send HTTP status code 404
            self.end_headers()                   # Send headers to finish the response

            # Open and send the contents of 404.html
            with open(f"{DIRECTORY}/404.html", "rb") as file:
                self.wfile.write(file.read())    # Write the file's content to the response
        else:
            # For other errors (e.g., 403, 500), use the default error handler
            super().send_error(code, message, explain)

# Create and start the HTTP server using TCP
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    # Display a message when the server starts
    print(f"Serving from {DIRECTORY} at http://localhost:{PORT}")
    
    # Keep the server running and listen for requests
    httpd.serve_forever()


# To run the server, use the command:
# python3 server.py

# To run from terminal, use:
# python3 -m http.server 8000