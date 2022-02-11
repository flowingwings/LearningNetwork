import random
import time
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverPort = 12000
serverSocket.bind(('', serverPort))
serverSocket.settimeout(1)
lastSeq = 0
recvNum = 0
loseNum = 0
clientOn = False
while True:
    try:
        message, address = serverSocket.recvfrom(1024)
        recvTime = time.time()
        message = message.decode()
        seq = int(message.split()[1])
        if seq != lastSeq + 1:
            loseNum += 1
        else:
            recvNum += 1
            clientOn = True
        lastSeq += 1
    except timeout:
        if clientOn:
            print("The client has stopped running.")
            break
print(
    "Received %d packets;" % recvNum,
    "Lost %d packets;" % loseNum,
    "AccRate: {}".format(float(recvNum) / float(recvNum + loseNum))
)
