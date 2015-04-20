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

global RAMSTRROUNDED
RAMTOTAL = int(SYSINFO.TotalPhysicalMemory) / (GBasMB)
RAMROUNDED = math.ceil(RAMTOTAL / 2.) * 2
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
	BODYSPECS = str(str(MODELPRNT) + str("\n") + str(HDDPRNT) + str("\n") + str(RAMPRNT) + str("\n") + str(CPUPRNT) + str("\n") + str(OSPRNT))

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
	global LISTCONTACT
	ASKCONTACT = "What contact name do you want listed? \n"
	LISTCONTACT = raw_input(ASKCONTACT)
	
	print("\r")
	global LISTINGEMAIL
	ASKEMAIL = "What email contact email will you be using? \n"
	LISTINGEMAIL = raw_input(ASKEMAIL)
	
	print("\r")
	global PHONENUMBER
	ASKNUMBA = "What telephone number do you want listed? \n"
	PHONENUMBER = raw_input(ASKNUMBA)
	
	print("\r")
	global PRICEDAT
	ASKPRICE = "How much are you selling the computer for? \n"
	PRICEDAT = raw_input(ASKPRICE)
	print("\r")
	print("Listing Name: " + LISTCONTACT)
	print("Listing Email:" + LISTINGEMAIL)
	print("Listing Phone Number: " + PHONENUMBER)
	print("Listing Asking Price: $" + PRICEDAT)
	print("Listing Title: " + LISTINGTITLE)

#------------------------ Selenium Webdriver Python Template for Auto Listing Craigslist -----------------------
	global craigslist_selenium_python_webdriver_header
	craigslist_selenium_python_webdriver_header = str('# -*- coding: utf-8 -*-'"\n"
	'import time'"\n"
	'from selenium import webdriver'"\n"
	'from selenium.webdriver.common.by import By'"\n"
	'from selenium.webdriver.common.keys import Keys'"\n"
	'from selenium.webdriver.support.ui import Select'"\n"
	'from selenium.common.exceptions import NoSuchElementException'"\n"
	'from selenium.common.exceptions import NoAlertPresentException'"\n"
	'import unittest, time, re'"\n"
	'	'"\n"
	'class Pythonwebdriverselenium(unittest.TestCase):'"\n"
	'	def setUp(self):'"\n"
	'		self.driver = webdriver.Firefox()'"\n"
	'		self.driver.implicitly_wait(30)'"\n"
	'		self.base_url = "https://post.craigslist.org/"'"\n"
	'		self.verificationErrors = []'"\n"
	'		self.accept_next_alert = True'"\n"
	'	'"\n"
	'	def test_pythonwebdriverselenium(self):'"\n"
	'		driver = self.driver'"\n"
	'		driver.get(self.base_url + "/k/DjV1fwDm5BG2R8qg6RDU3g/7qqew?s=edit")'"\n"
	'		driver.find_element_by_id("FromEMail").clear()'"\n"
	'		driver.find_element_by_id("FromEMail").send_keys("' + LISTINGEMAIL + '")'"\n"
	'		driver.find_element_by_id("ConfirmEMail").clear()'"\n"
	'		driver.find_element_by_id("ConfirmEMail").send_keys("' + LISTINGEMAIL + '")'"\n"
	'		driver.find_element_by_id("contact_phone_ok").click()'"\n"
	'		driver.find_element_by_id("contact_text_ok").click()'"\n"
	'		driver.find_element_by_id("contact_phone").clear()'"\n"
	'		driver.find_element_by_id("contact_phone").send_keys("' + PHONENUMBER + '")'"\n"
	'		driver.find_element_by_id("contact_name").clear()'"\n"
	'		driver.find_element_by_id("contact_name").send_keys("' + LISTCONTACT + '")'"\n"
	'		driver.find_element_by_id("PostingTitle").clear()'"\n"
	'		driver.find_element_by_id("PostingTitle").send_keys("' + LISTINGTITLE + '")'"\n"
	'		driver.find_element_by_id("Ask").clear()'"\n"
	'		driver.find_element_by_id("Ask").send_keys("' + PRICEDAT +'")'"\n"
	'		driver.find_element_by_id("GeographicArea").clear()'"\n"
	'		driver.find_element_by_id("GeographicArea").send_keys("' + str("LOCATION") + '")'"\n"
	'		driver.find_element_by_id("wantamap").click()'"\n"
	'		driver.find_element_by_id("postal_code").clear()'"\n"
	'		driver.find_element_by_id("postal_code").send_keys("' + str("ZIPCODE") + '")'"\n"
	'		driver.find_element_by_id("PostingBody").clear()'"\n")

	global craigslist_selenium_python_webdriver_body
	craigslist_selenium_python_webdriver_body = str(
	'		driver.find_element_by_id("PostingBody").send_keys("' +  str(str(MODELPRNT) + "        " + str(HDDPRNT) + "        " + str(RAMPRNT) + "        " + str(CPUPRNT)  + "        " + str(OSPRNT)) + '")'"\n"
	'		time.sleep(600)')

	global craigslist_selenium_python_webdriver_footer
	craigslist_selenium_python_webdriver_footer = str(
	'	'"\n"
	'	def is_element_present(self, how, what):'"\n"
	'		try: self.driver.find_element(by=how, value=what)'"\n"
	'		except NoSuchElementException, e: return False'"\n"
	'		return True'"\n"
	'	'"\n"
	'	def is_alert_present(self):'"\n"
	'		try: self.driver.switch_to_alert()'"\n"
	'		except NoAlertPresentException, e: return False'"\n"
	'		return True'"\n"
	'	'"\n"
	'	def close_alert_and_get_its_text(self):'"\n"
	'		try:'"\n"
	'			alert = self.driver.switch_to_alert()'"\n"
	'			alert_text = alert.text'"\n"
	'			if self.accept_next_alert:'"\n"
	'				alert.accept()'"\n"
	'			else:'"\n"
	'				alert.dismiss()'"\n"
	'			return alert_text'"\n"
	'		finally: self.accept_next_alert = True'"\n"
	'	'"\n"
	'	def tearDown(self):'"\n"
	'		self.driver.quit()'"\n"
	'		self.assertEqual([], self.verificationErrors)'"\n"
	'	'"\n"
	'if __name__ == "__main__":'"\n"
	'	unittest.main()'"\n"
	)

#------------------------------------------------ Where all the magic happens and/or everything is executed --------------------------------

def CRAIGSLISTCOREFUNCTION(): # Main processes involved in generating/posting a unique listing, from the above data, to Craigslist.
	CRAIGSLISTDETAILS()
	
	header = craigslist_selenium_python_webdriver_header
	body = craigslist_selenium_python_webdriver_body
	footer = craigslist_selenium_python_webdriver_footer
	
	appendscript = open('Craigslist_Output.py', 'w')
	appendscript.write(header)
	open('Craigslist_Output.py', 'wb')
	appendscript.write(body)
	open('Craigslist_Output.py', 'w')
	appendscript.write(footer)
	
	print('DONE.')
	
WHEREAREWELISTING()
#----------------------------------- Amazon Functions --------------------------------------------------