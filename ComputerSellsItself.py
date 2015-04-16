import os
import wmi
import math

c = wmi.WMI()    
SYSINFO = c.Win32_ComputerSystem()[0]
OSINFO = c.Win32_OperatingSystem()[0]
CPUINFO = c.Win32_Processor()[0]
HDDINFO = c.Win32_LogicalDisk()[0]

#------------------------------------ Basic Specifications Output & Format -------------------------------------

GBasMB = int(1000000000)

global MANUFACTURER
MANUFACTURER = SYSINFO.Manufacturer

global MODEL
MODEL = SYSINFO.Model

RAMTOTAL = int(SYSINFO.TotalPhysicalMemory) / (GBasMB)
RAMROUNDED = math.ceil(RAMTOTAL / 2.) * 2
global RAMSTRROUNDED
RAMSTRROUNDED = int(RAMROUNDED)

HDDTOTAL = int(HDDINFO.size) / (GBasMB) # rounding doesn't work
HDDROUNDED = math.ceil(HDDTOTAL / 2.) * 2

def ROUNDHDDTBORGB():
	global HDDTBORGBOUTPUT
	global HDDPRNT
	if HDDROUNDED >= 1000:
		HDDTBORGB = HDDROUNDED * .001
		HDDTBORGBOUTPUT = str(HDDTBORGB) + "TB"
		HDDPRNT = "HDD: " + str(HDDTBORGBOUTPUT)
		print(HDDPRNT)
	elif HDDROUNDED < 1000:
		HDDTBORGBOUTPUT = str(str(HDDROUNDED) + "GB")
		HDDPRNT = "HDD: " + str(HDDTBORGBOUTPUT)
		print(HDDPRNT)
	else:
		print("!ERROR!")

def CURRENTSPECS(): # Displays the end users raw input data for verification and accuracy of computers specs.
	print("\r")
	global MODELPRNT
	MODELPRNT = str("Model: " + MANUFACTURER + " " + MODEL)
	
	global RAMPRNT
	RAMPRNT = str("RAM: " + str(RAMSTRROUNDED) + "GB")
	
	global CPUPRNT
	CPUPRNT = str("CPU: " + CPUINFO.name)
	
	global OSPRNT
	OSPRNT = str("OS: " + OSINFO.caption)
	
	print MODELPRNT
	ROUNDHDDTBORGB()
	print RAMPRNT
	print CPUPRNT
	print OSPRNT

	global BODYSPECS
	BODYSPECS = str(MODELPRNT + "\r" + str(HDDPRNT) + "\r" + str(RAMPRNT) + "\r" + str(CPUPRNT) + "\r" + str(OSPRNT) + "\r")

	global LISTINGTITLE
	LISTINGTITLE = str(MANUFACTURER) + " " + str(MODEL) + " (" + str(RAMSTRROUNDED) + "GB RAM, " + str(HDDTBORGBOUTPUT) + " HDD)"
	
def WHEREAREWELISTING():
	CURRENTSPECS()
	print("\r")
	WHATWEBSITE = "Do you want to list on Amazon [1], Ebay [2], or Craigslist [3]? \n"
	ASKLISTING = raw_input(WHATWEBSITE)
	LOWERASKLISTINGINPUT = str(ASKLISTING.lower())
	
	if LOWERASKLISTINGINPUT == "amazon" or LOWERASKLISTINGINPUT == str(1):
		with open("amazon_listing_log", "a") as amazonlistings:
			amazonlistings.write(BODYSPECS)
		print("AMAZON")
	elif LOWERASKLISTINGINPUT == "ebay" or LOWERASKLISTINGINPUT == str(2):
		with open("ebay_listing_log", "a") as ebaylistings:
			ebaylistings.write(BODYSPECS)
		print("EBAY")
	elif LOWERASKLISTINGINPUT == "craigslist" or LOWERASKLISTINGINPUT == str(3):
		with open("craigslist_listing_log", "a") as craigslistlistings:
			craigslistlistings.write(BODYSPECS)
		CRAIGSLISTCOREFUNCTION()
	else:
		print(str(ASKLISTING) + " is not an option")

#------------------------------------ Craigslist Functions --------------------------------------------------

def CRAIGSLISTDETAILS(): # Displays the end users raw input for verification and accuracy of listing details and contact info.
	print("\r")
	ASKCONTACT = "What contact name do you want listed? \n"
	global LISTCONTACT
	LISTCONTACT = raw_input(ASKCONTACT)
	
	print("\r")
	ASKEMAIL = "What email contact email will you be using? \n"
	global LISTEMAIL
	LISTEMAIL = raw_input(ASKEMAIL)
	
	print("\r")
	ASKNUMBA = "What telephone number do you want listed? \n"
	global PHONENUMBER
	PHONENUMBER = raw_input(ASKNUMBA)
	
	print("\r")
	ASKPRICE = "How much are you selling the computer for? \n"
	global PRICEDAT
	PRICEDAT = raw_input(ASKPRICE)
	print("\r")
	print("Listing Name: " + LISTCONTACT)
	print("Listing Email:" + LISTEMAIL)
	print("Listing Phone Number: " + PHONENUMBER)
	print("Listing Asking Price: $" + PRICEDAT)
	print("Listing Title: " + LISTINGTITLE)

global craigslist_selenium_header
craigslist_selenium_header = str('<?xml version="1.0" encoding="UTF-8"?>'"\n"
'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">'"\n"
'<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">'"\n"
'<head profile="http://selenium-ide.openqa.org/profiles/test-case">'"\n"
'<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />'"\n"
'<link rel="selenium.base" href="http://minneapolis.craigslist.org/" />'"\n"
'<title>Computer Lists Itself</title>'"\n"
'</head>'"\n"
'<body>'"\n"
'<table cellpadding="1" cellspacing="1" border="1">'"\n"
'<thead>'"\n"
'<tr><td rowspan="1" colspan="3">Computer_Sells_Itself</td></tr>'"\n"
'</thead><tbody>)'"\n")

global craigslist_selenium_body_repeated
craigslist_selenium_body_repeated = str('<tr>'"\n"
'	<td>open</td>'"\n"
'	<td>/</td>'"\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>click</td>'"\n"
'	<td>css=a.sya.syp &gt; span.txt</td>'"\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>clickAndWait</td>'"\n"
'	<td>css=a.sya.syp &gt; span.txt</td>'"\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>click</td>'"\n"
'	<td>link=ALL COMPUTERS</td>'"\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>clickAndWait</td>'"\n"
'	<td>link=ALL COMPUTERS</td>'"\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>click</td>'"\n"
'	<td>link=post</td>'"\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>clickAndWait</td>'"\n"
'	<td>link=post</td>'"\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>click</td>'"\n"
"	<td>xpath=(//input[@name='id'])[6]</td>""\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>clickAndWait</td>'"\n"
"	<td>xpath=(//input[@name='id'])[6]</td>""\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>click</td>'"\n"
"	<td>xpath=(//input[@name='id'])[20]</td>""\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>clickAndWait</td>'"\n"
"	<td>xpath=(//input[@name='id'])[20]</td>""\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>click</td>'"\n"
'	<td>name=n</td>'"\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>clickAndWait</td>'"\n"
'	<td>name=n</td>'"\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>type</td>'"\n"
'	<td>id=FromEMail</td>'"\n"
'	<td>LISTINGEMAIL</td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>type</td>'"\n"
'	<td>id=FromEMail</td>'"\n"
'	<td>LISTINGEMAIL</td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>type</td>'"\n"
'	<td>id=ConfirmEMail</td>'"\n"
'	<td>LISTINGEMAIL</td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>type</td>'"\n"
'	<td>id=ConfirmEMail</td>'"\n"
'	<td>LISTINGEMAIL</td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>click</td>'"\n"
'	<td>id=contact_phone_ok</td>'"\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>click</td>'"\n"
'	<td>id=contact_phone_ok</td>'"\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>click</td>'"\n"
'	<td>id=contact_text_ok</td>'"\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>click</td>'"\n"
'	<td>id=contact_text_ok</td>'"\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>type</td>'"\n"
'	<td>id=contact_phone</td>'"\n"
'	<td>PHONENUMBA</td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>type</td>'"\n"
'	<td>id=contact_phone</td>'"\n"
'	<td>PHONENUMBA</td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>type</td>'"\n"
'	<td>id=contact_name</td>'"\n"
'	<td>CONTACTNAME</td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>type</td>'"\n"
'	<td>id=contact_name</td>'"\n"
'	<td>CONTACTNAME</td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>type</td>'"\n"
'	<td>id=PostingTitle</td>'"\n"
'	<td>POSTINGTITLE</td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>type</td>'"\n"
'	<td>id=PostingTitle</td>'"\n"
'	<td>POSTINGTITLE</td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>type</td>'"\n"
'	<td>id=Ask</td>'"\n"
'	<td>PRICE</td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>type</td>'"\n"
'	<td>id=Ask</td>'"\n"
'	<td>PRICE</td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>type</td>'"\n"
'	<td>id=GeographicArea</td>'"\n"
'	<td>COUNTYLOC</td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>type</td>'"\n"
'	<td>id=GeographicArea</td>'"\n"
'	<td>COUNTYLOC</td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>click</td>'"\n"
'	<td>id=wantamap</td>'"\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>click</td>'"\n"
'	<td>id=wantamap</td>'"\n"
'	<td></td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>type</td>'"\n"
'	<td>id=postal_code</td>'"\n"
'	<td>POSTAL</td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>type</td>'"\n"
'	<td>id=postal_code</td>'"\n"
'	<td>POSTAL</td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>type</td>'"\n"
'	<td>id=PostingBody</td>'"\n"
'	<td>POSTINGBODY</td>'"\n"
'</tr>'"\n"
'<tr>'"\n"
'	<td>type</td>'"\n"
'	<td>id=PostingBody</td>'"\n"
'	<td>POSTINGBODY</td>'"\n"
'</tr>'"\n")

global craigslist_selenium_footer
craigslist_selenium_footer = str('</tbody></table>'"\n"
'</body>'"\n"
'</html>'"\n")

def CRAIGSLISTCOREFUNCTION(): # Main processes involved in generating/posting a unique listing, from the above data, to Craigslist.
	CRAIGSLISTDETAILS()
    
	html_header = craigslist_selenium_header
	body_repeat = craigslist_selenium_body_repeated
	html_footer = craigslist_selenium_footer

	lenghead = str(len(html_header))
	lengbody = str(len(body_repeat))
	lengfoot = str(len(html_footer))

	print("\r")
	print("Selenium Header Length: ") + lenghead
	print("Selenium Body Length: ") + lengbody
	print("Selenium Footer Length: ") + lengfoot

	craigslistinfo = [[MODELPRNT,HDDPRNT,RAMPRNT,CPUPRNT,OSPRNT,PHONENUMBER,LISTCONTACT,LISTINGTITLE,PRICEDAT,LISTEMAIL]]

	final_html = ""
	final_html += html_header

	for line in craigslistinfo:
		model_numba = line[0]
		hdd_capacity = line[1]
		ram_capacity = line[2]
		cpu_specs = line[3]
		os_type = line[4]
		phone_numba = line[5]
		listed_name = line[6]
		posting_title = line[7]
		askingprice = line[8]
		listing_email = line[9]
		final_html += str(body_repeat.replace('LISTINGEMAIL',listing_email).replace('PHONENUMBA',phone_numba).replace('CONTACTNAME',listed_name).replace('POSTINGTITLE',posting_title).replace('PRICE',askingprice).replace('POSTINGBODY',model_numba + "\r" + hdd_capacity + "\r" + ram_capacity + "\r" + cpu_specs + "\r" + os_type))
	
	final_html += html_footer
    
	with open('Craigslist_Output','w+') as f:
		f.write(final_html)
	
	print('DONE.')
	
WHEREAREWELISTING()
#----------------------------------- Amazon Functions --------------------------------------------------