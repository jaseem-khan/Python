from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time
import allure
from allure_commons.types import AttachmentType

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):
    
    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        print("classSetup method run")

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        # login process
        self.lp.login("test@email.com", "abcabc")
        allure.attach(self.driver.get_screenshot_as_png(), name="HomeScreen", attachment_type=AttachmentType.PNG)
        time.sleep(3)
        # result1 = self.lp.verifyTitle()
        # self.ts.mark(result1, "Title is incorrect")
        # result2 = self.lp.verifyLoginSuccess()
        # self.ts.markFinal("test_validLogin", result2, "Login was successful")

    @pytest.mark.run(order=1)
    def test_loginFailed(self):
        self.lp.login(email="abc@gmail.com")
        time.sleep(3)
        result = self.lp.verifyLoginFailed()
        assert result == True
        allure.attach(self.driver.get_screenshot_as_png(), name="testLoginFailed", attachment_type=AttachmentType.PNG)


