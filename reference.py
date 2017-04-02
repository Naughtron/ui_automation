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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
# imports to run Selenium headless
from pyvirtualdisplay import Display


# selenium test for /create_account
# verify: posts, and page name
class verify_home_title(unittest.TestCase):
    def setUp(self):
        # self.display = Display(visible=0, size=(800, 600))
        # self.display.start()
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

    # self.display.stop()


class create_new_account(unittest.TestCase):
    # test setup
    def setUp(self):
        # self.display = Display(visible=0, size=(800, 600))
        # self.display.start()
        # create faker
        fake = Faker()
        # create rand string
        rand_string = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(10)])
        # create user data:
        u_name = fake.name()
        spl_name = HumanName(u_name)
        self.f_uname = spl_name.first
        self.l_uname = spl_name.last
        self.usr_email = spl_name.first + spl_name.last + "@notrealemail.com"
        self.disp_name = spl_name.first + spl_name.last + rand_string
        self.u_password = "4lw4ysb3" + rand_string
        self.driver = webdriver.Chrome()
        self.server = "https://www.oreilly.com/"

    # test create new account
    def test_validate_click_home(self):
        driver = self.driver
        server = self.server
        driver.get(server)
        
        #user data
        fst_username = self.f_uname
        lst_username = self.l_uname
        disp_name = self.disp_name
        email_addy = self.usr_email
        usr_passwrd = self.u_password
        
        # wait for the create button to render on page
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "log-out"))
            )
        except:
            print "failed to load."        
        
        # get to the create page
        r_logout = driver.find_element_by_id('log-out')
        r_logout.click()
        

        # wait for at least one form element to render on page
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "capture_signIn_traditionalSignIn_createButton"))
            )
        except:
            print "failed to load."
            
        # create new account button click
        crt_acct_button = driver.find_element_by_xpath("//input[@value='Create Account']")
        crt_acct_button.click()
            
        # fill out new user form
        r_first_name = driver.find_element_by_id('capture_traditionalRegistration_traditionalRegistration_firstName')
        r_first_name.send_keys(fst_username)

        r_last_name = driver.find_element_by_id(
            'capture_traditionalRegistration_form_item_traditionalRegistration_lastName')
        r_last_name.send_keys(lst_username)

        r_display_name = driver.find_element_by_id(
            'capture_traditionalRegistration_form_item_traditionalRegistration_displayName')
        r_display_name.send_keys(disp_name)

        r_email = driver.find_element_by_id(
            'capture_traditionalRegistration_form_item_traditionalRegistration_emailAddress')
        r_email.send_keys(email_addy)

        r_password_og = driver.find_element_by_id(
            'capture_traditionalRegistration_form_item_traditionalRegistration_password')
        r_password_og.send_keys(usr_passwrd)

        r_password_cfm = driver.find_element_by_id(
            'capture_traditionalRegistration_form_item_traditionalRegistration_passwordConfirm')
        r_password_cfm.sendKsend_keys(usr_passwrd)


if __name__ == '__main__':
    unittest.main()
