import BaseHTTPServer

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    
    Page = """
<html>
<body>
<p>Hello, web! </p>
</body>
</html>
"""
    # Obradi GET request
    def do_GET(self):
        page = self.create_page()
        self.send_page(page)

    def create_page(self):
        page = self.Page
        return page
    def send_page(self, page):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Lenght", str(len(page)))
        self.end_headers()
        self.wfile.write(page)

if __name__ == '__main__':
    print "Starting web server..."
    serverAdress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAdress, RequestHandler)
    server.serve_forever()

