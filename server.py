import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer

class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    server = HTTPServer(('0.0.0.0', port), NoCacheHandler)
    print(f"Server listening on http://0.0.0.0:{port} with zero-cache headers")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
