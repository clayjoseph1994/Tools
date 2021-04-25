#Python code for socket practice

#importing socket and sys modules
import socket
import sys

#Setting host and port variables for server based on user input
host = input ("Type the server IP address: ")
port = int(input("Type the server port #: "))

#Create socket based on inet4 family address and TCP connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    #Bind socket to user specified host addr and port num
    s.bind((host, port))
# Return error message if bind fails, and exit
except socket.error as msg:
    print('Bind failed')
    sys.exit()

#Indicate successful bind of socket 
print("# Socket bind complete")

#Setting the number of queued connections to the socket listening for a connection
s.listen(3)
print("# Socket now listening")

#Accepting incoming connections, returning the socket object (conect) and the client address bound to the socket (addr)
connect, addr = s.accept()

#Print the info describing how the client is connected to the server socket
print('# Connected to ' + addr[0] + ':' + str(addr[1]))

#Iterate over the data sent between the server and client, and continue to print as long as there is data being transmitted
#When no data exists, close the connection
while True:     
    data = connect.recv(1024)
    line = data.decode('UTF-8')    # convert to string
    line = line.replace("\n","")   # remove newline character
    print(line)

s.close()