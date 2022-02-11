import datetime
import threading
from socket import *
import sys

serverPort = 12000
# Fill starts
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
# Fill ends
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(10000)  # Filled
        print(message.decode())
        filename = message.split()[1]
        f = open(filename[1:])
        outputData = f.read()  # Filled
        # Fill starts
        GMT_FORMAT = "%a, %d %b %Y %H:%M:%S GMT"
        time = datetime.datetime.utcnow().strftime(GMT_FORMAT)
        header = ("HTTP/1.1 200 OK\n"
                  "Connection: close\n"
                  "Date: "
                  + time +
                  "\n"
                  "Server: BoboServer/0.0.1 (Windows 10)\r\n"
                  # "Content-Length: 1024\r\n"
                  "Content-Type: text/html\r\n\r\n")
        connectionSocket.send(header.encode())
        # Fill ends
        for i in range(0, len(outputData)):
            # print("outputData[%d]: " % i + outputData[i], end='')
            connectionSocket.send(outputData[i].encode())
            # print(" sent")
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill starts
        errorMessage = ("HTTP/1.1 404 Not Found\r\n"
                        "Connection: close\r\n")
        connectionSocket.send(errorMessage.encode())
        # Fill ends
        # Close client socket
        # Fill starts
        connectionSocket.close()
        # Fill ends
        # print("Connection Failed...")

serverSocket.close()
sys.exit()
