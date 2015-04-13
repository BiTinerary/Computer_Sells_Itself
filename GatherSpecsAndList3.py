import os
import wmi
import math

c = wmi.WMI()    
SYSINFO = c.Win32_ComputerSystem()[0]
OSINFO = c.Win32_OperatingSystem()[0]
CPUINFO = c.Win32_Processor()[0]
HDDINFO = c.Win32_LogicalDisk()[0]
RAMINFO = c.Win32_PhysicalMemory()[0]

"""
------------------------------------ Basic Specifications Output & Format -------------------------------------
"""

global MANUFACTURER
MANUFACTURER = SYSINFO.Manufacturer
global MODEL
MODEL = SYSINFO.Model
RAMTOTAL = int(SYSINFO.TotalPhysicalMemory)
global RAMROUNDED
RAMROUNDED = math.ceil(RAMTOTAL / 2000000000.) * 2.000000000
HDDTOTAL = int(HDDINFO.size)
global HDDROUNDED
HDDROUNDED = math.ceil(HDDTOTAL / 2000000000.) * 2.000000000

def CURRENTSPECS(): # Displays the end users raw input data for verification and accuracy of computers specs.
	print("\r")
	global MODELPRNT
	MODELPRNT = str("Model: " + MANUFACTURER + " " + MODEL)
	global HDDPRNT
	HDDPRNT = str("HDD: " + str(HDDROUNDED) + "GB")
	global RAMPRNT
	RAMPRNT = str("RAM: " + str(RAMROUNDED) + "GB")
	global CPUPRNT
	CPUPRNT = str("CPU: " + CPUINFO.name)
	global OSPRNT
	OSPRNT = str("OS: " + OSINFO.caption)
	print MODELPRNT
	print HDDPRNT
	print RAMPRNT
	print CPUPRNT
	print OSPRNT
	global STORECURRENTSPECSFORMAT
	STORECURRENTSPECSFORMAT = str(MODELPRNT + "\r" + HDDPRNT + "\r" + RAMPRNT + "\r" + CPUPRNT + "\r" + OSPRNT + "\r")

def WHEREAREWELISTING():
	CURRENTSPECS()
	print("\r")
	WHATWEBSITE = "Do you want to list on Amazon [1], Ebay [2], or Craigslist [3]? \n"
	ASKLISTING = raw_input(WHATWEBSITE)
	LOWERASKLISTINGINPUT = str(ASKLISTING.lower())
	
	if LOWERASKLISTINGINPUT == "amazon" or LOWERASKLISTINGINPUT == str(1):
		with open("amazon_listing_log", "a") as amazonlistings:
			amazonlistings.write(STORECURRENTSPECSFORMAT)
		print("AMAZON")
	elif LOWERASKLISTINGINPUT == "ebay" or LOWERASKLISTINGINPUT == str(2):
		with open("ebay_listing_log", "a") as ebaylistings:
			ebaylistings.write(STORECURRENTSPECSFORMAT)
		print("EBAY")
	elif LOWERASKLISTINGINPUT == "craigslist" or LOWERASKLISTINGINPUT == str(3):
		with open("craigslist_listing_log", "a") as craigslistlistings:
			craigslistlistings.write(STORECURRENTSPECSFORMAT)
		CRAIGSLISTCOREFUNCTION()
	else:
		print(str(ASKLISTING) + " is not an option")
"""
------------------------------------ Craigslist Functions --------------------------------------------------
"""

def CRAIGSLISTDETAILS(): # Displays the end users raw input for verification and accuracy of listing details and contact info.
	print("\r")
	ASKCONTACT = "What contact name do you want listed? \n"
	global LISTCONTACT
	LISTCONTACT = raw_input(ASKCONTACT)
	
	print("\r")
	ASKNUMBA = "What telephone number do you want listed? \n"
	global PHONENUMBA
	PHONENUMBA = raw_input(ASKNUMBA)
	
	print("\r")
	ASKPRICE = "How much are you selling the computer for? \n"
	global PRICEDAT
	PRICEDAT = raw_input(ASKPRICE)
	
	print("\r")
	global TITLE
	TITLE = str(str(MANUFACTURER) + " " + str(MODEL) + " (" + str(RAMSIZE) + "GB RAM, " + str(HDDSIZE) + "GB HDD)")
	print("Listing Name: " + LISTCONTACT)
	print("Listing Phone Number: " + PHONENUMBA)
	print("Listing Asking Price: $" + PRICEDAT)
	print("Listing Title: " + TITLE)

def CRAIGSLISTCOREFUNCTION(): # Main processes involved in generating/posting a unique listing, from the above data, to Craigslist.
	CRAIGSLISTDETAILS()
	with open('craigslist_selenium_header.txt','r') as a, open('craigslist_selenium_body_repeated.txt','r') as b, open('craigslist_selenium_footer.txt','r') as c:
    
		html_header = a.read()
		body_repeat = b.read()
		html_footer = c.read()

	lenghead = str(len(html_header))
	lengbody = str(len(body_repeat))
	lengfoot = str(len(html_footer))

	print("\r")
	print("Selenium Header Length: ") + lenghead
	print("Selenium Body Length: ") + lengbody
	print("Selenium Footer Length: ") + lengfoot

	craigslistinfo = [[MODELPRNT,HDDPRNT,RAMPRNT,CPUPRNT,OSPRNT,PHONENUMBA,LISTCONTACT,TITLE,PRICEDAT]]

	final_html = ""
	final_html += html_header

	for line in craigslistinfo:
		model_numba = line[0]
		hdd_capacity = line[1]
		ram_capacity = line[2]
		cpu_specs = line[3]
		os_type = line[4]
		telenumba = line[5]
		listedname = line[6]
		postedtitle = line[7]
		askingprice = line[8]
		final_html += str(body_repeat.replace('POSTINGBODY',model_numba + "\r" + hdd_capacity + "\r" + ram_capacity + "\r" + cpu_specs + "\r" + os_type).replace('PHONE',telenumba).replace('CONTACTNAME',listedname).replace('POSTINGTITLE',postedtitle).replace('PRICE',askingprice))
	
	final_html += html_footer
    
	with open('Craigslist_Output','w+') as f:
		f.write(final_html)
	
	print('DONE.')
	
WHEREAREWELISTING()

"""
------------------------------------ Amazon Functions --------------------------------------------------
"""

