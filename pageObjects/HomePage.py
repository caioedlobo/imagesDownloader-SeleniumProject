from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver


    paste = (By.XPATH, "//li[@class='sc-1arpg0p-3 UwJcB']")
    url = "https://savee.it/lara_/boards/"


    def getPaste(self, index):
        return self.driver.find_element_by_xpath("(//li[@class='sc-1arpg0p-3 UwJcB'])" + "[" + str(index + 1) + "]").click()

    def getImage(self):
        return self.driver.find_elements(*HomePage.paste)

    def getURL(self):
        return self.driver.get(HomePage.url)