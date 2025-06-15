#coding:utf-8

import http.server 
import socketserver

port = 90
address = ("", port)

server = http.server.HTTPServer

#handler = http.server.SimpleHTTPRequestHandler
handler = http.server.CGIHTTPRequestHandler
#httpd = socketserver.TCPServer(address, handler)

handler.cgi_directories = ["/"]
httpd = server(address, handler)

print(f"Serveur demarre sur le port {port} ")
httpd.serve_forever()