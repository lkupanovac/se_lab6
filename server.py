import BaseHTTPServer
import os

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    # Obradi GET request
    def do_GET(self):
        #os.getcwd -> get_current_working_directory
        #self.path -> putanja do filea kojeg browser trazi
        print os.getcwd() + self.path
        try:
            if self.path == "/":
                full_path = os.getcwd() + "/index.html"
            else:
                full_path = os.getcwd() + self.path
            
            if not os.path.exists(full_path):
                raise Exception ("%s not found" %self.path)
            elif os.path.isfile(full_path):
                self.handle_file(full_path)
        except Exception as msg:
            self.handle_error(msg)
    def handle_error (self, msg):
        self.send_response(404)
        self.send_header("Content-Type", "text/html")
        page= "<html><body><p>" + str(msg)+ "</p></body></html>"
        self.send_header("content-Lenght", str(len(page)))
        self.end_headers()
        self.wfile.write(page)
            
        

    def send_page(self, page):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Lenght", str(len(page)))
        self.end_headers()
        self.wfile.write(page)
    def handle_file(self, path):
        try:
            with open(path, "rb") as reader:
                content = reader.read()
            self.send_page(content)
        except IOError as msg:
            msg = "Nevalja!"

if __name__ == '__main__':
    print "Starting web server..."
    serverAdress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAdress, RequestHandler)
    server.serve_forever()

