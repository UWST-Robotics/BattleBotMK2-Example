import socket
from time import sleep
UDP_IP = "10.10.20.200"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

from imports.controller import XboxController
joy = XboxController()



    #Smooths inputs from 1.0 to -1.0 float to -100 to 100 integer


while True:
    data = joy.read()
    data[0] = (int) (data[0] *10)
    data[1] = (int) (data[1] *10)
    data[2] = (int) (data[2] *10)
    data[3] = (int) (data[3] *10)

    #Creates send data lx,ly,rt,lt
    #Converts list to string without []
    data = str(data).strip("[]")
    #encodes and with ASCII
    sendData = f"{data}".encode("ASCII")
    #Sends data
    print(f"message: {data}")
    sock.sendto(sendData, (UDP_IP, UDP_PORT))
    sleep(.0166 * 2) #Loops about 30 times a second