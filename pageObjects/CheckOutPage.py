from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConFirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    finalCheckOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutItems(self):
        return self.driver.find_element(*CheckOutPage.checkOut)

    def finalCheckOutItems(self):
        self.driver.find_element(*CheckOutPage.finalCheckOut).click()
        return ConFirmPage(self.driver)  # Returning the next page class object
