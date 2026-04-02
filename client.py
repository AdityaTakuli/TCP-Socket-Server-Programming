import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  #get the host name no hardcoded ip address
HEADER = 64 #bytes
FORMAT = "utf-8" #64 byte 
ADDR = (SERVER,PORT) #in a tuple 
DISCONNNECT_NAME = "Disconnect me"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT);
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER-len(send_length));
    
    client.send(send_length)
    client.send(message)
    

send("Hello")