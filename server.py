import socket
import threading


PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  #get the host name no hardcoded ip address
HEADER = 64 #bytes
FORMAT = "utf-8" #64 byte 
ADDR = (SERVER,PORT) #in a tuple
DISCONNNECT_NAME = "Disconnect me"

#print(f"HOST NAME: {socket.gethostname()}")


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #making new socket

#binding of the socket with teh port and ip adress
server.bind(ADDR)

def handle_client(conn, addr): #handles individual clients
    print(f"[NEW CONNECTION] {addr} conected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #blocking lines of code that is why we need threading
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT) #formatting the data and decoding it             
            if msg == DISCONNNECT_NAME:
                connected = False
            
            print(f"[{addr}] {msg}")
        
    conn.close() #server_object.close
        
        
def start(): #handles the server staring clients and tell them which thread to go to
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() 
        #accept() -> (socket object, address info)
        # Wait for an incoming connection. Return a new socket representing 
        # the connection, and the address of the client. For IP sockets, 
        # the address info is a pair (hostaddr, port).
        
        #start the threading 1 thread -> one client 
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        #target=handle_client → which function to run
        # args=(conn, addr) → what arguments to pass later
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")
        
         

print(f"[STARTING] server is stating.....")
start()



