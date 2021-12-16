import inspect
import logging
import os
import urllib.request
from urllib.parse import urlparse

import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:


    def downloadImage(self, image):
        url = image.get_attribute('src')
        filename = urlparse(url)
        urllib.request.urlretrieve(url, filename=os.path.basename(filename.path))

    def createDirectory(self, name):
        os.chdir("C:\\pythonProject\\imagesDownloader\\files")
        if '/' in name:
            name = name.replace("/", "_")
        os.mkdir(name)
        os.chdir(name)

    def moveToNextImage(self):
        self.driver.find_element_by_xpath("//body[@class='no-touch']").send_keys(Keys.ARROW_RIGHT)


    def getLogger(self):
        loggerName = inspect.stack()[1][3]  # colocar o nome do arquivo em vez de __name__
        logger = logging.getLogger(loggerName)  # vai pegar o nome do arquivo que está sendo usado
        # logger = logging.getLogger(__name__)

        fileHandler = logging.FileHandler('logfile.log', mode='w')
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s :%(message)s")  # levelname é o erro, info, warning...?
        fileHandler.setFormatter(formatter)  # conecta o formatter com o fileHandler

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger