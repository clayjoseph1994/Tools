import http.client

print("This program returns a list of methods is OPTIONS is enabled")

host = input("Host IP: ")
port = input("Port(default=80): ")

if(port == ""):
    port = 80

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request("OPTIONS", "/")
    response = connection.getresponse()
    print("Enabled methods: ", response.getheader("allow"))
    connection.close()
except ConnectionRefusedError:
    print("Oops, the connection failed")