import socket
from socket import *
import time

serverName = "localhost"
serverPort = 12000
serverAddr = (serverName, serverPort)
clientSocket = socket(AF_INET, SOCK_DGRAM)
RTTList = []
for i in range(1, 11):
    sendTime = time.time_ns()
    pingMessage = "Heartbeat " + str(i) + " " + str(sendTime)
    clientSocket.sendto(pingMessage.encode(), serverAddr)
    print("Sending Message: " + pingMessage)
    time.sleep(0.2)
clientSocket.close()
