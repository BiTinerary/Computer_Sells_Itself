# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
	
class Pythonwebdriverselenium(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url = "https://post.craigslist.org/"
		self.verificationErrors = []
		self.accept_next_alert = True
	
	def test_pythonwebdriverselenium(self):
		driver = self.driver
		driver.get(self.base_url + "/k/DjV1fwDm5BG2R8qg6RDU3g/7qqew?s=edit")
		driver.find_element_by_id("FromEMail").clear()
		driver.find_element_by_id("FromEMail").send_keys("56161@biti.com")
		driver.find_element_by_id("ConfirmEMail").clear()
		driver.find_element_by_id("ConfirmEMail").send_keys("56161@biti.com")
		driver.find_element_by_id("contact_phone_ok").click()
		driver.find_element_by_id("contact_text_ok").click()
		driver.find_element_by_id("contact_phone").clear()
		driver.find_element_by_id("contact_phone").send_keys("9874547154")
		driver.find_element_by_id("contact_name").clear()
		driver.find_element_by_id("contact_name").send_keys("zipidydo")
		driver.find_element_by_id("PostingTitle").clear()
		driver.find_element_by_id("PostingTitle").send_keys("Acer Aspire TC-105 (8GB RAM, 1.0TB HDD)")
		driver.find_element_by_id("Ask").clear()
		driver.find_element_by_id("Ask").send_keys("999")
		driver.find_element_by_id("GeographicArea").clear()
		driver.find_element_by_id("GeographicArea").send_keys("LOCATION")
		driver.find_element_by_id("wantamap").click()
		driver.find_element_by_id("postal_code").clear()
		driver.find_element_by_id("postal_code").send_keys("ZIPCODE")
		driver.find_element_by_id("PostingBody").clear()
		driver.find_element_by_id("PostingBody").send_keys("Model: Acer Aspire TC-105        HDD: 1.0TB        RAM: 8GB        CPU: AMD A8-6500 APU with Radeon(tm) HD Graphics            OS: Microsoft Windows 8")
		time.sleep(600)	
	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException, e: return False
		return True
	
	def is_alert_present(self):
		try: self.driver.switch_to_alert()
		except NoAlertPresentException, e: return False
		return True
	
	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally: self.accept_next_alert = True
	
	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)
	
if __name__ == "__main__":
	unittest.main()
