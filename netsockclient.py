import socket

host = input ("Type the server IP address: ")
port = int(input("Type the server port #: "))

client_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_s.connect((host, port))
print("Connection established with server")

mess = input("Type message to send to server: ")
client_s.sendall(mess.encode())

# Look for the response
amount_received = 0
amount_expected = len(mess)

while amount_received < amount_expected:
    data = client_s.recv(16)
    amount_received += len(data)
    print(data)

client_s.close()