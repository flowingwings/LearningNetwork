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
    pingMessage = "Ping " + str(i) + " " + str(sendTime)
    clientSocket.sendto(pingMessage.encode(), serverAddr)
    print("Sending Message: " + pingMessage)
    clientSocket.settimeout(1)
    try:
        modifiedMsg, serverAddress = clientSocket.recvfrom(1024)
        recvTime = time.time_ns()
        print(modifiedMsg.decode())
        RTT = recvTime - sendTime
        RTTList.append(RTT)
        print("Response received. \nRecv time: %f."
              " \nRTT: %f" % (recvTime, RTT))
        # Quite strange...
        # The RTT would only be among 2 values:
        # 0, or about 1000000 (with some little fluctuation).
        # I think that's because the RTT is less than 1 ms,
        # but can't figure out the resource of the fluctuation.
    except timeout:
        print("Request timed out")
    finally:
        print()
if len(RTTList):
    minRTT = min(RTTList)
    maxRTT = max(RTTList)
    avgRTT = sum(RTTList) / 10.0
    packetLossRate = (10.0 - len(RTTList)) / 10.0
    print(
        "Minimum RTT: %f ns" % minRTT,
        "Maximum RTT: %f ns" % maxRTT,
        "Average RTT: %f ns" % avgRTT,
        "{0:.1f}%".format(packetLossRate * 100),
        sep='\n'
    )
clientSocket.close()
