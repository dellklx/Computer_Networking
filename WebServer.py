from socket import *
serverSocket = socket(AF_INET,SOCK_STREAM)
serverPort = 6789
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

while True:
    print('Ready to serve...')
    connectionSocket,addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.decode().split()
        print(filename)
        f = open(filename[1][1:])
        outputdata = f.read()
        header = ' HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (len(outputdata))
        connectionSocket.send(header.encode())

        for i in range(0,len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()

    except IOError:
        header = ' HTTP/1.1 404 Not Found'
        connectionSocket.send(header.encode())
        connectionSocket.close()

serverSocket.close()