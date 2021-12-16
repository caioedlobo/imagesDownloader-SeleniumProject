import time
import urllib.request


from pynput.keyboard import Key, Controller

from pageObjects.HomePage import HomePage
from pageObjects.PastePage import PastePage
from utilities.BaseClass import BaseClass



class TestDownload2(BaseClass):

    def test_download2(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        pastes = homePage.getImage()
        pastePage = PastePage(self.driver)

        for paste in range(len(pastes)):

            homePage.getPaste(paste)
            directory = pastePage.getTitleText()

            self.createDirectory(directory)
            image = pastePage.getImage()
            image.click()
            for i in range(pastePage.getPasteSize() + 1):
                image_hr = pastePage.getHighResolutionImage()
                self.downloadImage(image_hr)
                self.moveToNextImage()

            #image.clear()
            homePage.getURL()













