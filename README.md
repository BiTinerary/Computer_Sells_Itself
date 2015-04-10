# Laptop_Sells_Itself
The general idea to this script is a further addition to my hardware tester. The hardware tester does exactly that. Test the absolute basic integrity of a Windows machine (Keyboard, speakers, WiFi, Battery, etc...)

From here, since I'm in an Ecommerce setting, I've decided to automate the selling/listing process each of the machines I test undergoes. This is accomplished through the "Laptop_Sells_Iteself" script.

I've integrated native Windows Powershell commands into a more universal language, Python. The powershell commands gather the specifications of the host computer, assigns them to a series of variables. These variables are tucked into an array which replaces keywords (more variables) of a Selenium .HTML script. Producing an automated Selenium script that will [eventually] post, or filter, these specifications and post listings on Amazon/Ebay/Craigslist. I've started with craigslist because it doesn't have an .API and requires more hardcoding to get the job done. In a nutshell, if I can automate craigslist then I can automate an Ebay or Amazon listing.

The scripting process goes something like this.

1: run on target computer. CHECK.<br>
2: output log file. CHECK.<br>
3: run on a different target computer. CHECK.<br>
4: append log file. CHECK.<br>
5: python stores log file details as a variable. NOT DONE BUT NEXT.<br>
6: python consults this variable for each item in list. CHECK.<br>
7: python replaces strings in selenium template with each target itieration. CHECK.<br>
8: Each selenium template for Amazon/Ebay/CL is stored seperately from one another (as logs?)<br>
9: However they are also stored in one master file per script execution.

Possible implementations:
~ Automatically compile a python script through selenium webdriver.<br>
~ At end of functions, construct a "master" .exe using Py2Exe.<br>
11: Execute master .exe file. CHECK.
