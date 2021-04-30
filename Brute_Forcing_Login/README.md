This program is a brute forcing tool I wrote to get the login credentials of this simple web page
It used HTTP Auth and one of the users passwords was just the department they were in

You can see here in the screenshot that the webpage had a table of users already, and the user's respective depts: ![Web Page](https://github.com/clayjoseph1994/Tools/blob/main/Brute_Forcing_Login/images/site.png)

The point of the script I created was to pull this information from the page, separate it into two different lists, parse the data to filter out the html and make it text-only, then throw those lists at the HTTP login page at "admin.php" (found by clicking the "Admin Area" hyperlink below the table)

Running the brute_force.py program resulted in the following: ![Script Results](https://github.com/clayjoseph1994/Tools/blob/main/Brute_Forcing_Login/images/Got_creds.png)

Once I found the username and password resulting in a 200 response, I used those credentials for the login, resulting in: ![Successful Login](https://github.com/clayjoseph1994/Tools/blob/main/Brute_Forcing_Login/images/successful_login.png)

This was a super simple program, but creating it taught me useful skills such as how to use the requests module and beautiful soup, as well as how to rewrite a program based in python2 to python3
