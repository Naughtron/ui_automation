# -*- coding: UTF-8 -*-
# imports
import unittest
import unicodedata
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
        self.driver = webdriver.Chrome()
        self.server = "https://www.safaribooksonline.com/"

    # simple verification of page title
    def test_validate_page_elements(self):
        driver = self.driver
        server = self.server
        title_assert = "Safari, the world's most comprehensive tech & business learning platform"
        driver.get(server)
        # strip unicode from title
        title = unicodedata.normalize('NFKD', driver.title).encode('ascii', 'ignore')
        # assert the title is correct
        self.assertIn(title_assert, title)

    def tearDown(self):
        self.driver.close()

    # self.display.stop()


class user_signin(unittest.TestCase):
    # test setup
    def setUp(self):
        
        # create user data:
        self.username = "my.email@gmail.com"
        self.password = "XXXXXXXXXXX"
        self.server = "https://www.safaribooksonline.com/"
        self.driver = webdriver.Chrome()

    # test create new account
    def test_validate_click_home(self):
        driver = self.driver
        server = self.server
        username = self.username
        password = self.password
        driver.get(server)
        
        # click on the sign in button: 
        sign_in = driver.find_element_by_class_name("login")
        sign_in.click()
        
        # find username elem and send name
        user_name = driver.find_element_by_id("id_email")
        user_name.send_keys(username)
        # find password elem and send password
        password_box = driver.find_element_by_id("id_password1")
        password_box.send_keys(password)
        # click the login button
        sign_in_button = driver.find_element_by_css_selector('.button.with-chevron.js-login-button')
        sign_in_button.click()
        # assert we are logged in
        current_url = driver.current_url
        conv_url = str(current_url)
        self.assertEqual(conv_url, "https://www.safaribooksonline.com/home/")
        

if __name__ == '__main__':
    unittest.main()
