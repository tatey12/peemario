import http.server
import socketserver
import random

PORT = 8069
print("ill be alive at http://18.223.24.247" + str(PORT))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("im alive at http://18.223.24.247" + str(PORT))
    httpd.serve_forever()
