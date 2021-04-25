#Python code for socket practice

#importing socket module
import socket

#Setting host and port variables for server based on user input
host = input ("Type the server IP address: ")
port = int(input("Type the server port #: "))

#Create socket based on inet4 family address and TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind socket to user specified host addr and port num
s.bind((host, port))

#Setting the number of queued connections to the socket listening for a connection
s.listen(1)

#Output to let the user know the socket server is awaiting a connection
print("Server has started; awaiting connection...")

#Accepting incoming connections, returning the socket object (conect) and the client address bound to the socket (addr)
connect, addr = s.accept()

#Print the info describing how the client is connected to the server socket
print("Connected at ", addr)

#Iterate over the data sent between the server and client, and continue to print as long as there is data being transmitted
#When no data exists, close the connection
while 1:
    data = connect.recv(1024)
    if not data: break
    connect.sendall(b'<---Message--->\n')
    print(data.decode('utf-8'))
connect.close()