from selenium import webdriver

chrome_driver_path ="C:\Developement\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)
# driver.close()

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n]={
       "time":event_times[n].text,
       "name":event_names[n].text,
}

print(events)
driver.quit()
