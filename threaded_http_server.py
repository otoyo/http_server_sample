import time
import socket
import threading
import SocketServer

class MyHTTPRequestHandler(SocketServer.StreamRequestHandler):

    def handle(self):
        data = self.rfile.readline().strip()
        print data
        
        cur_thread = threading.currentThread()
        print "Current thread:", cur_thread.getName()

        f = open("index.html", 'r')

        self.wfile.write("HTTP/1.1 200 OK\r\n")
        self.wfile.write("Content-Type: text/html; charset=utf-8\r\n")
        self.wfile.write("\r\n")
        self.wfile.write(f.read())

        f.close()

class ThreadedHTTPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 0

    server = ThreadedHTTPServer((HOST, PORT), MyHTTPRequestHandler)
    ip, port = server.server_address

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()

    print "Server loop running in thread:", server_thread.getName()
    print "IP: %s" % ip
    print "Port: %s" % port

    time.sleep(60)
