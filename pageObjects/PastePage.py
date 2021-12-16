from selenium.webdriver.common.by import By


class PastePage():
    def __init__(self, driver):
        self.driver = driver

    image = (By.XPATH, "(//img[@class='sc-1g1a8y9-2 dntmGl'])")
    image_high_resolution = (By.XPATH, "//img[@class='sc-1onld9v-11 kLSOsR'][2]")
    close_button = (By.XPATH, "//a[@title='Close (⎋)']")
    title = (By.XPATH, "//span[@class='sc-1oxracf-1 evgbES']")
    size = (By.XPATH, "//span[@class='aa67q4-4 eQZHbf']")



    def getListImages(self):
        return self.driver.find_elements(*PastePage.image)

    def getImage(self):
        return self.driver.find_element(*PastePage.image)

    def getHighResolutionImage(self):
        return self.driver.find_element(*PastePage.image_high_resolution)

    def closeImage(self):
        return self.driver.find_element(*PastePage.close_button).click()

    def getTitleText(self):
        return self.driver.find_element(*PastePage.title).text

    def getPasteSize(self):
        size_text = self.driver.find_element(*PastePage.size).text
        size = size_text.split()
        size_paste = int(size[0])
        return size_paste





