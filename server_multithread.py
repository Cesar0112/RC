from socket import *
import threading

def handle_request(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename [1:], "r")
        outputdata = f.read()
        #si esta bien manda 200
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    
    #si detecta erro manda 404
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.close()

def start_server():
    #prepara el socket
    serverSocket = socket(AF_INET, SOCK_STREAM)


    serverSocket.bind(('', 3001))
    #establece el numero de conexiones permitidas
    serverSocket.listen(5)


    while True:
        #establece la conexion
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        t = threading.Thread(target=handle_request, args=(connectionSocket,))
        t.start()

# empieza el servidor
start_server()