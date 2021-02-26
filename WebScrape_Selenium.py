# by Tech With Tim
# https://www.youtube.com/watch?v=b5jt2bhSeXs

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Applications/chromedriver"
# important: for Mac users: write the name of the file without extension exe!: "chromdriver"
# important: for Mac users: because the chromedriver was not dowloaded from apple store, it might be blocked
# to unblock: Apple menu => system preferences => Security & Privacy => give allowence "Allow apps downloaded from:"


driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN) # hitting "enter"

# print(driver.page_source) # displays source code of the web page, than we can access anything from that page


time.sleep(5) # we needed to import time module, the program will wait 5 second before it executes next line of code - "quiting"

driver.quit() # quiting the whole browser

# if we gonna access some elements from html, we access it usually in this order
# 1) ID (is unigue)
# 2) Name (dont neccessarily is unigue)
# 3) class
# problem with selenium is that if we access elements that are not unique it will return the first element that is available




 
