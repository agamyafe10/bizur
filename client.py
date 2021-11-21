import socket
import hashlib
from hashlib import md5


def str_to_hash(client_input="Hello World!"):
    hash_object = hashlib.md5(client_input.encode())
    hashed_code = hash_object.hexdigest()
    print(hashed_code)
    return hashed_code

def start_hashing(fromnum,to):
    for i in range(fromnum, to):
        if str_to_hash(str(i)) == "cc4af25fa9d2d5c953496579b75f6f6c":
            print("Your Number is:{0}",i)
            break

def Main():

    hocmst='192.168.11.154' #client ip
    port = 4000
    
    server = ('192.168.11.152', 4005)
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((hocmst,port))
    
    message = input("-> ")
    while message !='q':
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Received from server: " + data)
        message = input("-> ")
    s.close()

if _name=='main_':
    Main()
