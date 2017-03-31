# imports
import requests
import unittest
import sys
from selenium import webdriver
# imports to run Selenium headless
from pyvirtualdisplay import Display

# unit test class
'''setup'''
class TestHelloWorld(unittest.TestCase):
	server_address = ''

	def setUp(self):
		self.server_address = "localhost:5000"

	def test_HelloWorld(self):
		url_template = 'http://%s'
		url = url_template %(self.server_address)

		# verify url
		#print url

		# make the request
		resp = requests.get(url)

		# import pdb; pdb.set_trace()

		# assert response
		self.assertEqual(resp.status_code, 200)
		# assert text coming back
		self.assertEqual(resp.text, u'Hello World!')

# unit test for /mod2
class TestModTwoPageContents(unittest.TestCase):
	server_address = ''

	def setUp(self):
		self.server_address = "localhost:5000"

	def test_mod2(self):
		url_template = 'http://%s/mod2'
		url = url_template %(self.server_address)

		#print url

		resp = requests.get(url)
		#import pdb; pdb.set_trace()

		self.assertEqual(resp.status_code, 200)
		# this is just a bad assert self.assertEqual(resp.text, u'<!--this is the first template \n<html>\n <head>\n \t<title>Home - microblog</title>\n </head>\n <body>\n \t<h1>Hello, Naughtron!</h1>\n </body>\n</html> -->\n\n<!-- user Jinja to set control statements in a template-->\n<!--<html>\n <head>\n \t \n \t<title>Home - microblog</title>\n \t\n </head>\n <body>\n \t<h1>Greetings, Naughtron!</h1>\n \t \n \t<p>Jeff says: <b>Be the bomb you throw!</b></p> \n \t \n \t<p>Connor says: <b>I am a real life lore nerd</b></p> \n \t \n </body>\n</html>-->\n\n<!--inherit from the base template-->\n<!--this is the base template that allows other templates to inherit core features-->\n<!-- the index.html will inherit from this template-->\n<html>\n <head>\n \t\n \t<title>Home - microblog</title>\n \t\n </head>\n <body>\n \t<div>Microblog: <a href="/index">Home</a></div>\n \t<hr>\n \t\n<h1>Greetings, Naughtron!</h1>\n\n<div><p>Jeff says: <b>Be the bomb you throw!</b></p></div>\n\n<div><p>Connor says: <b>I am a real life lore nerd</b></p></div>\n\n\n </body>\n</html>')

# unit tests for mod 3
class TestLoginIsUp(unittest.TestCase):
	server_address = ''

	def setUp(self):
		self.server_address = "localhost:5000"

	def test_login_page_is_there(self):
		url_template = 'http://%s/login'
		url = url_template %(self.server_address)

		#print url
		resp = requests.get(url)

		# assert
		self.assertEqual(resp.status_code, 200)


# selenium test for /mod2
# verify: posts, and page name
class TestMod2Selenium(unittest.TestCase):
	def setUp(self):
		self.display = Display(visible=0, size=(800, 600))
		self.display.start()
		self.driver = webdriver.Firefox()

	# simple verification of page title
	def test_validate_page_elements(self):
		driver = self.driver
		driver.get("http://127.0.0.1:5000/mod2")
		self.assertIn("Home - microblog", driver.title)
	def tearDown(self):
		self.driver.close()
		self.display.stop()

class TestMod2HomeClick(unittest.TestCase):
	# test setup
	def setUp(self):
		self.display = Display(visible=0, size=(800, 600))
		self.display.start()
		self.driver = webdriver.Firefox()
	# test
	def test_validate_click_home(self):
		driver = self.driver
		driver.get("http://127.0.0.1:5000/mod2")
		# find the home line
		home_link = driver.find_element_by_css_selector('a[href="/index"]')
		home_link.click()
		#assertEqual(driver.title,"Home - microblog")

if __name__ == '__main__':
    unittest.main()
