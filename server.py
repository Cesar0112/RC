from socket import *

#crea un socket tcp
serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort=3000

serverSocket.bind(('',serverPort))

#a lo mas se escucha 1
serverSocket.listen(1)
print('the web server is up on port:',serverPort)

while True:
	#Ser up a new connection from the client
	print('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()

	try:
		#recieve the request message from the client
		message = connectionSocket.recv(1024)
		
		filename = message.split()[1]
		
		f = open(filename[1:])
		outputdata = f.read()
		connectionSocket.send(bytes('HTTP/1.1 200 OK','UTF-8'))
		
		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(bytes(outputdata[i],'UTF-8'))
		connectionSocket.send(bytes("\r\n",'UTF-8'))
		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		print('file not found')
		connectionSocket.send(bytes('\nHTTP/1.1 404 Not Found\n','UTF-8'))
		connectionSocket.send(bytes('<html><head><title>First Web Page</title></head><body><h1>404 Not Found</h1></body></html>\r\n','UTF-8'))
		connectionSocket.close()
