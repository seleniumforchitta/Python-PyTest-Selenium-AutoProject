from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        # Creating All Objects of the Page Classes.
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        # We have called the Next Page object from this method only as by clicking "Shop",
        # - we go to the next page. I.e. checkout page -  so this methods returns the object
        log.info("Getting all card titles - ")
        cards = checkoutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()

        # Click First CheckOut
        checkoutPage.checkOutItems().click()

        # Click Final CheckOut
        confirmPage = checkoutPage.finalCheckOutItems()
        # - we go to the next page. I.e. confirm page -  so this methods returns the object

        log.info("Entering country Name.")
        confirmPage.inputCountry().send_keys("ind")
        # self.driver.find_element_by_id("country").send_keys("ind")
        self.verifyLinkPresence("India")  # Pass the text for which you are waiting using EC

        confirmPage.chooseCountry().click()
        confirmPage.clickCheckBox().click()
        confirmPage.clickPurchaseBtn().click()
        textMatch = confirmPage.getSuccessMsg().text
        log.info("Text received - "+textMatch)

        assert ("Success! Thank you!" in textMatch)
        log.info("Console Message - Test Completed Successfully")

