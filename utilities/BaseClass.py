import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)  # __name__ will capture the testcase file name.
        # if you don't give anything, it will print root

        fileHandler = logging.FileHandler('logFile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")

        fileHandler.setFormatter(formatter)  # Give format information to logger object
        logger.addHandler(fileHandler)  # fileHandler object - in which file, it has to print
        logger.setLevel(logging.DEBUG)  # set the level of logging
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.LINK_TEXT, text)))
        # it is getting the Link Text from the calling methods.

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)