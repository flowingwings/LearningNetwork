from socket import *

serverName = "localhost"
serverPort = 12000
serverAddr = (serverName, serverPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(serverAddr)
header = (
    "GET /test.html HTTP/1.1\n"
    "Host: "
    + "192.168.0.104" + "\n" +
    "User-agent: BoboClient/0.0.1\n"
    "Accept-language: en,zh-CN,zh-TW\n\r\n"
)
clientSocket.send(header.encode())
response = b''
# This cycle is necessary! But I don't know why.
# If the clientSocket only receives once,
# the connection would be closed in advance out of expectation,
# many bytes would be lost and server would get WinError 10024.
# The lost bytes always start from the 2nd char in HTML,
# where the reason of the bug may hides. TODO
while True:
    recv = clientSocket.recv(10000)
    if not recv:
        break
    response += recv
print(response.decode())
clientSocket.close()