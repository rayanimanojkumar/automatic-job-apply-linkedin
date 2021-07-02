from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "****"
ACCOUNT_PASSWORD = "**"
PHONE = "***"
chrome_driver_path ="C:\Developement\chromedriver.exe"
driver = webdriver.Chrome(executable_path= chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2611364275&f_AL=true&geoId=102713980&keywords=marketing%20internship&location=India")

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(3)

email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)
#
# remember_button = driver.find_element_by_css_selector("footer button")
# remember_button.click()

time.sleep(3)

apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()




phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)


submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()
#
# next_button = driver.find_element_by_css_selector("footer button")
# next_button.click()


# first_name = driver.find_element_by_name("fName")
# first_name.send_keys("manoj")
# second_name = driver.find_element_by_name("lName")
# second_name.send_keys("kumar")
# email = driver.find_element_by_name("email")
# email.send_keys("manojkumar55@gmail.com")
#
# submit = driver.find_element_by_css_selector("form button")
# submit.click()
# article_count = driver.find_element_by_css_selector("#articlecount a")
# # article_count.click()
#
# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()
# search = driver.find_element_by_name("search")
# search.send_keys("corona virus")
# search.send_keys(Keys.ENTER)
