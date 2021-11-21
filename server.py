import socket
from _thread import *
import threading


def Main():
   
    host = '192.168.11.152' #Server ip
    port = 4005

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server Started")
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Message from: " + str(addr))
        print("From connected user: " + data)
        data = data.upper()
        print("Sending: " + data)
        s.sendto(data.encode('utf-8'), addr)
    s.close()

if __name__=='__main__':
    Main()