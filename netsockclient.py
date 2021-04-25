#import socket and sys
import socket
import sys

#input server information
host = input ("Type the server IP address: ")
port = int(input("Type the server port #: "))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

#Notify of connection with server
print("Connection established with server")

#ALlow data to be continually sent until the program is exited
while True:
    mess = input("Type message to send to server: ")
    s.sendall(mess.encode())

s.close()