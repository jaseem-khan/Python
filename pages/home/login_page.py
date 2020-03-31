from selenium.webdriver.common.by import By
from selenium import webdriver
from base.selenium_driver import SeleniumDriver
import logging
import utilities.custom_logger as cl

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "//input[@id='user_email']"
    _pass_field = "//input[@id='user_password']"
    _login_button = "//input[@name='commit']"

    def getLogLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._login_link)

    def getEmailField(self):
        return self.driver.find_element(By.XPATH, self._email_field)

    def getPassField(self):
        return self.driver.find_element(By.XPATH, self._pass_field)

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, self._login_button)

    def getTitle(self):
        return self.driver.title

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, "xpath")

    def enterPass(self, password):
        self.sendKeys(password, self._pass_field, "xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, "xpath")

    def login(self, email="", password=""):
        self.driver.get("https://learn.letskodeit.com/")
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPass(password)
        self.clickLoginButton()

    def verifyLoginSuccess(self):
        result = self.isElementPresent("//img[@class='gravatar']", locatorType="xpath")
        self.log.info("Login successfully")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[@class='alert alert-danger']", locatorType="xpath")
        self.log.info("Login failed")
        return result

    def verifyTitle(self):
        if "Google" in self.getTitle():
            return True
        else:
            return False




