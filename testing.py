import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.implicitly_wait(8)

driver.get("https://savee.it/lara_/boards/archival-images-of-flight-and-space-2/")
time.sleep(3)
driver.find_element_by_xpath("//div[@class='dw68ul-1 gUawzv']").click()
driver.find_element_by_xpath("//body[@class='no-touch']").send_keys(Keys.ARROW_RIGHT)

