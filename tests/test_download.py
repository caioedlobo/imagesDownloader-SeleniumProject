import time
import urllib.request

from selenium.webdriver import ActionChains

from pageObjects.HomePage import HomePage
from pageObjects.PastePage import PastePage
from utilities.BaseClass import BaseClass

import requests
from PIL import Image
from io import StringIO


class TestDownload(BaseClass):

    def test_download(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)

        pastes = homePage.getImage()

        pastePage = PastePage(self.driver)
        #cont = 0
        for paste in range(len(pastes)):
            cont = 0
            #time.sleep(3)
            #pastes[cont].click()
            homePage.getPaste(paste)
            directory = pastePage.getTitleText()
            self.createDirectory(directory)
            image = pastePage.getListImages()
            #print(pastePage.getPasteSize())
            image_list = []
            size = pastePage.getPasteSize()
            while(size != len(image_list)):
                #if image[cont].get_attribute('src') not in image_list:
                    #image_list.append(image[cont].get_attribute('src'))
                #log.info(pastePage.getPasteSize())
                #log.info(pastePage.getTitleText())
                #actions = ActionChains(self.driver)
                #actions.move_to_element(image[i]).perform()
                #var = image[i]
                #image[i].location_once_scolled_into_view
                    #try:


                try:
                    image[cont].click()     #clica na imagem para ampliar
                #except:
                    #self.driver.execute_script("window.scrollTo(0, 1000)")
                    #self.driver.execute_script("arguments[0].scrollIntoView();", image[cont])
                    #image[cont].click()
                    image_hr = pastePage.getHighResolutionImage()       #pega o link para download da imagem ampliada
                    if image_hr not in image_list:
                        image_list.append(image_hr)

                        self.downloadImage(image_hr)
                    pastePage.closeImage()

                except:
                    cont = 0
                    self.driver.execute_script("window.scrollTo(0, 500)")
                    image = pastePage.getListImages()
                #log.info(image_hr.get_attribute('src'))
                #url = pastePage.getListImages().get_attribute('src')
                #urllib.request.urlretrieve(url, url)
                ##self.downloadImage(image_hr)
                ##pastePage.closeImage()

                #cont+=1
                #else:
                    #cont = 0
                    #self.driver.execute_script("window.scrollTo(0, 200)")




                cont += 1

            image.clear()
            homePage.getURL()













