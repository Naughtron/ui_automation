from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.oreilly.com/")

r_logout = driver.find_element_by_id('log-out')
r_logout.click()

# enter user information
r_create_acct = driver.find_element_by_id('capture_signIn_traditionalSignIn_createButton')
r_create_acct.click()

r_first_name = driver.find_element_by_id('capture_traditionalRegistration_traditionalRegistration_firstName')
r_first_name.sendKeys("Chris")

r_last_name = driver.find_element_by_id('capture_traditionalRegistration_form_item_traditionalRegistration_lastName')
r_last_name.sendKeys("Naughton")

r_display_name = driver.find_element_by_id('capture_traditionalRegistration_form_item_traditionalRegistration_displayName')
r_display_name.sendKeys("Naughtron")

r_email = driver.find_element_by_id('capture_traditionalRegistration_form_item_traditionalRegistration_emailAddress')
r_email.sendKeys('chris.naughton+seTest@gmail.com')

r_password_og = driver.find_element_by_id('capture_traditionalRegistration_form_item_traditionalRegistration_password')
r_password_og.sendKeys("4lw4ysb3t3st1ng")

r_password_cfm = driver.find_element_by_id('capture_traditionalRegistration_form_item_traditionalRegistration_passwordConfirm')
r_password_cfm.sendKeys("4lw4ysb3t3st1ng")

# submit the info
crt_acct_btn = driver.find_element_by_id("capture_traditionalRegistration_createAccountButton")
crt_acct_btn.click()

# validate
acct_page = s.xpath('//div[@class="navheaderbg"]/h1').extract()
