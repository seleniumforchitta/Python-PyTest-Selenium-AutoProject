from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:
    # We are bringing the control of the driver from actual testcase to here. For that we are creating a constructor
    # - and we will pass the driver while creating the object in the actual test case.
    def __init__(self, driver):
        self.driver = driver

    #  Here we have click on the shop object
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']:nth-child(2)")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    option = (By.CSS_SELECTOR, "input[value='option1']")
    submitbtn = (By.XPATH, "//input[@class='btn btn-success']")
    successmsg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click() # This line is same as below
        # driver.find_element_by_link_text("Shop")
        # * is used so that it will deserialize the shop while putting it as a locator
        return CheckOutPage(self.driver)
        # Above. We are returning the next page class object i.e. checkout page

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getOption(self):
        return self.driver.find_element(*HomePage.option)

    def getSubmitBtn(self):
        return self.driver.find_element(*HomePage.submitbtn)

    def getSuccessMsg(self):
        return self.driver.find_element(*HomePage.successmsg)

