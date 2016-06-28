import socket
import re
import threading
import sys, getopt
import os
import time

class ThreadedServer(object):
    def __init__(self, host, port, directory, clienttimeout = 60, socklisten = 5):
        self.host = host
        self.port = port
	self.directory = directory
	self.clienttimeout = clienttimeout
	self.socklisten = socklisten
        
    def listen(self):
	self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(self.socklisten)
        while True:
            client, address = self.sock.accept()
	    print "Connection from: " + `address`
            client.settimeout(self.clienttimeout)
            threading.Thread(target = self.listenToClient,args = (client,)).start()

    def RetrFile(self, client, fileName):
	try:		
		
		filePath = self.directory + '/' + fileName
        	f = open(filePath, 'rb')
		print(filePath)
	except IOError:
		print("in except")
		errorMsg = "File could not be found!"
		client.sendall(errorMsg)
		client.close()
	match = re.match('.*\.(.*)', fileName)
	fileType = match.group(1)

	if(fileType == 'py' or fileType == 'txt'):
		client.sendall("""HTTP/1.1 200 OK
Server: SLAVI
Content-Type: text/plain\n
""")
	elif(fileType == "html" or fileType == "php"):
		client.sendall("""HTTP/1.1 200 OK
Server: SLAVI
Content-Type: text/html\n
""")
	elif(fileType == 'png'):
		client.sendall("""HTTP/1.1 200 OK
Server: SLAVI
Content-Type: image/png\n
""")
	elif(fileType == 'jpg'):
		client.sendall("""HTTP/1.1 200 OK
Server: SLAVI
Content-Type: image/jpeg\n
""")
	
	while True:
		fileData = f.read()
		if fileData == '': break
		client.sendall(fileData)
	f.close()   

    def listenToClient(self, client):
        while True:
            try:
                req = client.recv(4096)
		print (req)
                match = re.match('GET .*?.=(\d+)', req)
		if match:
			client.sendall("""HTTP/1.1 200 OK
Server: SLAVI
Content-Type: text/html\n""")
			a = match.group(1)
			print "a: " + a

			match = re.match('GET .*&.=(\d+) HTTP', req)
			if match:
				b = match.group(1)
				print "b: " + b
				sumOfBoth = int(a) + int(b)
				print "a + b = %s" % (sumOfBoth)
				print "\n"
				client.sendall("""
<html>
<body>
<p><b> sum: %d </b></p>
</body>
</html>""" % (sumOfBoth))
				client.close()

		else:
			match = re.match('GET /(.*) ', req)
			fileName = match.group(1)
			self.RetrFile(client, fileName)
			client.close()
            except:
                client.close()

if __name__ == "__main__":
	host = '' 
	port = '8080'
	directory = '/home'
	#get port and folder from cmd line
	try:
		opts, args = getopt.getopt(sys.argv[1:],"hp:f:",["port=", "directory="])		
	except getopt.GetoptError:
		print 'webserver1.py -p <port> -f <directory>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'webserver1.py -p <port> -f <directory>'
			sys.exit()
	    	elif opt in ("-p", "--port"):
			port = arg
		elif opt in ("-f", "--directory"):
			directory = arg
	port = int(port)
	if (port>=64000 or port<=1): 
			print("should specify port as parameter!")
			sys.exit()
	if not os.path.isdir(directory):
		print("not a valid directory")
		sys.exit()
		
	print("                      **********SERVER STARTED**********")
	ThreadedServer('', port, directory).listen()



























