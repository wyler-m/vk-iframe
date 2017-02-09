# adapated from http://www.piware.de/2011/01/creating-an-https-server-in-python/
# generate seperate key+crt files, make sure common name (CN) == ip or hostname
#    openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout newkey.key -out newkey.crt
#    openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout zulu.key -out zulu.crt
# run as follows:
#    python simple-https-server.py


import BaseHTTPServer, SimpleHTTPServer
import ssl

httpd = BaseHTTPServer.HTTPServer(('localhost', 8000), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='/Users/rmetge/pypro/javascript projects/vk-iframe/key.pem', server_side=True)
httpd.serve_forever()