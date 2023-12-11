import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log = self.getlogger()
        # Creating All Objects of the Page Classes.
        homePage = HomePage(self.driver)
        log.info("Filling data in the form - ")
        homePage.getName().send_keys(getData["firstName"])
        log.info("firstName is - "+getData["firstName"])
        homePage.getEmail().send_keys(getData["EmailID"])
        homePage.getPassword().send_keys(getData["Password"])
        homePage.getCheckbox().click()
        self.selectOptionByText(homePage.getGender(), getData["Gender"])
        # The above method id created inside base Class as a reusable function
        homePage.getOption().click()
        homePage.getSubmitBtn().click()
        # Printing the alert message below.
        message = homePage.getSuccessMsg().text
        print(message)
        log.info("Console Message - "+message)
        # Lets do assertion
        assert "Success" in message
        if "Success" in message:
            print("Test case is Passed !")
            log.info("Console Message - Test Completed Successfully")
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    def getData(self, request):
        return request.param
