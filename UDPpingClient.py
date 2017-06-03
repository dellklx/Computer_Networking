from socket import *
import time
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
for i in range(10):
    sendTime = time.time()
    message = '%s------%s' %(i,sendTime)
    clientSocket.sendto(message.encode(),(serverName,serverPort))
    modifiedMessage,serverAddress = clientSocket.recvfrom(1024)
    rtt = time.time() - sendTime
    if modifiedMessage.decode() == 'lost':
        print('Sequence %d: Request time out' % (i + 1))
    else:
        print('Sequence %d : Reply from %s    RTT=%.3fs' %(i+1,serverName,rtt))
clientSocket.close()