from selenium.webdriver.common.by import By


class ConFirmPage:

    def __init__(self, driver):
        self.driver = driver

    insertCountry = (By.CSS_SELECTOR, "#country")
    clickCountry = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseBtn = (By.CSS_SELECTOR, "[type='submit']")
    successMsg = (By.CSS_SELECTOR, "[class*='alert-success']")

    def inputCountry(self):
        return self.driver.find_element(*ConFirmPage.insertCountry)

    def chooseCountry(self):
        return self.driver.find_element(*ConFirmPage.clickCountry)

    def clickCheckBox(self):
        return self.driver.find_element(*ConFirmPage.checkBox)

    def clickPurchaseBtn(self):
        return self.driver.find_element(*ConFirmPage.purchaseBtn)

    def getSuccessMsg(self):
        return self.driver.find_element(*ConFirmPage.successMsg)
