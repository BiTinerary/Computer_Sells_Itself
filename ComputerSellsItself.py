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

global RAMSTRROUNDED
RAMTOTAL = int(SYSINFO.TotalPhysicalMemory) / (GBasMB)
RAMROUNDED = math.ceil(RAMTOTAL / 2.) * 2
RAMSTRROUNDED = int(RAMROUNDED)

global HDDROUNDED
HDDTOTAL = int(HDDINFO.size) / (GBasMB) # rounding doesn't work
HDDROUNDED = math.ceil(HDDTOTAL / 2.) * 2

global HDDPRNT
global HDDTBORGBOUTPUT
if HDDROUNDED >= 1000:
	HDDTBORGB = HDDROUNDED * .001
	HDDTBORGBOUTPUT = str(HDDTBORGB) + "TB"
	HDDPRNT = "HDD: " + str(HDDTBORGBOUTPUT)
elif HDDROUNDED < 1000:
	HDDTBORGBOUTPUT = str(str(HDDROUNDED) + "GB")
	HDDPRNT = "HDD: " + str(HDDTBORGBOUTPUT)

#------------------------------- CraigsDetails for Log and listing info ---------------

def COMPUTERDETAILS(): # Displays the end users raw input for verification and accuracy of listing details and contact info.
	
	global MODELPRNT
	MODELPRNT = str("Model: " + MANUFACTURER + " " + MODEL)
	
	global RAMPRNT
	RAMPRNT = str("RAM: " + str(RAMSTRROUNDED) + "GB")
	
	global CPUPRNT
	CPUPRNT = str("CPU: " + CPUINFO.name)
	
	global OSPRNT
	OSPRNT = str("OS: " + OSINFO.caption)
	
	print("\r")
	print MODELPRNT
	print HDDPRNT
	print RAMPRNT
	print CPUPRNT
	print OSPRNT
	
	global BODYSPECS
	BODYSPECS = str(str(MODELPRNT) + str("\n") + str(HDDPRNT) + str("\n") + str(RAMPRNT) + str("\n") + str(CPUPRNT) + str("\n") + str(OSPRNT))

# --------------------- Determine where the target computer will be listed ---------------------

def WHEREAREWELISTING():
	print("\r")
	WHATWEBSITE = "Do you want to list on Amazon [1], Ebay [2], or Craigslist [3]? \n"
	ASKLISTING = raw_input(WHATWEBSITE)
	LOWERASKLISTINGINPUT = str(ASKLISTING.lower())
	
	if LOWERASKLISTINGINPUT == "amazon" or LOWERASKLISTINGINPUT == str(1):
		print("AMAZON")
	elif LOWERASKLISTINGINPUT == "ebay" or LOWERASKLISTINGINPUT == str(2):
		print("EBAY")
	elif LOWERASKLISTINGINPUT == "craigslist" or LOWERASKLISTINGINPUT == str(3):
		CRAIGSLISTCOREFUNCTION()
	else:
		print(str(ASKLISTING) + " is not an option")
		
#---------------------------------------------------------------

def CRAIGSLISTCOREFUNCTION(): # Main processes involved in generating/posting a unique listing, from the above data, to Craigslist.
	global LOGSEPERATION
	LOGSEPERATION = "-------------------------------------"
	
	global LISTINGTITLE
	LISTINGTITLE = str(MANUFACTURER) + " " + str(MODEL) + " (" + str(RAMSTRROUNDED) + "GB RAM, " + str(HDDTBORGBOUTPUT) + " HDD)"
	
	print("\r")
	ASKCONTACT = "What contact name do you want listed? \n"
	global LISTCONTACT
	LISTCONTACT = raw_input(ASKCONTACT)
	
	print("\r")
	ASKEMAIL = "What email contact email will you be using? \n"
	global LISTINGEMAIL
	LISTINGEMAIL = raw_input(ASKEMAIL)
	
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
	print("Listing Email:" + LISTINGEMAIL)
	print("Listing Phone Number: " + PHONENUMBER)
	print("Listing Asking Price: $" + PRICEDAT)
	print("Listing Title: " + LISTINGTITLE)
	
	with open("craigslist_listing_log", "a") as craigslistlistings:
		craigslistlistings.write(str("\n"))
		craigslistlistings.write(str(BODYSPECS) + str("\r\n"))
		craigslistlistings.write(str("Listing Name: " + LISTCONTACT) + str("\n"))
		craigslistlistings.write(str("Listing Email: " + LISTINGEMAIL) + str("\n"))
		craigslistlistings.write(str("Listing Phone Number: " + PHONENUMBER) + str("\n"))
		craigslistlistings.write(str("Listing Asking Price: $" + PRICEDAT) + str("\n"))
		craigslistlistings.write(str("Listing Title: " + LISTINGTITLE) + str("\r"))
		craigslistlistings.write(LOGSEPERATION)
	
	global stupidseleniumsyntax
	stupidseleniumsyntax = str("'id'")
	
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
	'		self.base_url = "https://www.craigslist.org"'"\n"
	'		self.verificationErrors = []'"\n"
	'		self.accept_next_alert = True'"\n"
	'	'"\n"
	'	def test_pythonwebdriverselenium(self):'"\n"
	'		driver = self.driver'"\n"
	'		driver.get(self.base_url + "/")'"\n"
	'		driver.find_element_by_css_selector("#postlks > li > #post").click()'"\n"
	'		driver.find_element_by_xpath("(//input[@name=' + stupidseleniumsyntax + '])[6]").click()'"\n"
	'		driver.find_element_by_xpath("(//input[@name=' + stupidseleniumsyntax + '])[20]").click()'"\n"
	'		driver.find_element_by_name("n").click()'"\n"
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
	
	header = craigslist_selenium_python_webdriver_header
	body = craigslist_selenium_python_webdriver_body
	footer = craigslist_selenium_python_webdriver_footer
	
	craigslistoutputfilename = str('Craigslist Output '+MODEL+'.py')
	appendscript = open(craigslistoutputfilename, 'w')
	appendscript.write(header)
	open(craigslistoutputfilename, 'wb')
	appendscript.write(body)
	open(craigslistoutputfilename, 'w')
	appendscript.write(footer)
	print('DONE.')

COMPUTERDETAILS()
WHEREAREWELISTING()
#----------------------------------- Amazon Functions --------------------------------------------------