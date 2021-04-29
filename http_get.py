import http.client

print("This program returns a list of methods is OPTIONS is enabled")

host = input("Host IP: ")
port = input("Port(default=80): ")
url = input("URL for GET request: ")

if(port == ""):
    port = 80

try:
    connection = http.client.HTTPConnection(host, port)
    connection.request("GET", url)
    response = connection.getresponse()
    print("Response from server: ", response.status)
    connection.close()
except ConnectionRefusedError:
    print("Oops, the connection failed")