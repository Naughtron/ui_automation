# -*- coding: UTF-8 -*-
# imports
import unittest
import unicodedata
import sys
import uuid
import random
import string
import time
from faker import Faker
from nameparser import HumanName
from selenium import webdriver
# imports to run Selenium headless
from pyvirtualdisplay import Display

# selenium test for /create_account
# verify: posts, and page name
class verify_home_title(unittest.TestCase):
	def setUp(self):
		#self.display = Display(visible=0, size=(800, 600))
		#self.display.start()
		self.driver = webdriver.Chrome()
		self.server = "https://www.oreilly.com/"

	# simple verification of page title
	def test_validate_page_elements(self):
		driver = self.driver
		server = self.server
		title_assert = "OReilly Media - Technology and business training, knowledge, and insight, delivered by experts and innovators"
		driver.get(server)
		# strip unicode from title
		title = unicodedata.normalize('NFKD', driver.title).encode('ascii', 'ignore')
		# assert the title is correct
		self.assertIn(title_assert, title)
		
	def tearDown(self):
		self.driver.close()
		#self.display.stop()

class create_new_account(unittest.TestCase):
	# test setup
	def setUp(self):
		#self.display = Display(visible=0, size=(800, 600))
		#self.display.start()
		# create faker
		fake = Faker()
		# create rand string
		rand_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(10)])
		# create user data: 
		u_name = fake.name()
		spl_name = HumanName(u_name)
		f_uname = spl_name.first
		l_uname = spl_name.last
		usr_email = f_uname + l_uname + "@notrealemail.com"
		disp_name = f_uname + l_uname + rand_string
		u_password = "4lw4ysb3" + rand_string
		self.driver = webdriver.Chrome()
		self.server = "https://www.oreilly.com/"
	# test create new account
	def test_validate_click_home(self):
		driver = self.driver
		server = self.server
		driver.get(server)
		# get to the create page
		r_logout = driver.find_element_by_id('log-out')
		r_logout.click()
		time.sleep(2)
		# click on create new account
		r_create_acct = driver.find_element_by_id('capture_signIn_traditionalSignIn_createButton')
		r_create_acct.click()
		# fill out new user form
		r_first_name = driver.find_element_by_id('capture_traditionalRegistration_traditionalRegistration_firstName')
		r_first_name.sendKeys(f_uname)
		
		r_last_name = driver.find_element_by_id('capture_traditionalRegistration_form_item_traditionalRegistration_lastName')
		r_last_name.sendKeys(l_uname)
		
		r_display_name = driver.find_element_by_id('capture_traditionalRegistration_form_item_traditionalRegistration_displayName')
		r_display_name.sendKeys(disp_name)
		
		r_email = driver.find_element_by_id('capture_traditionalRegistration_form_item_traditionalRegistration_emailAddress')
		r_email.sendKeys(usr_email)
		
		r_password_og = driver.find_element_by_id('capture_traditionalRegistration_form_item_traditionalRegistration_password')
		r_password_og.sendKeys(u_password)
		
		r_password_cfm = driver.find_element_by_id('capture_traditionalRegistration_form_item_traditionalRegistration_passwordConfirm')
		r_password_cfm.sendKeys(u_password)		
		
		
		
		
if __name__ == '__main__':
	unittest.main()
