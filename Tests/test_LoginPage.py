import pytest
from selenium import webdriver

from Config.config import TestData
from Pages.LoginPage import LoginPage
from Config.config import*

class Test_Login():
    driver = webdriver.Chrome(executable_path = r"C:\Users\Weronika\OWASP ZAP\webdriver\windows\32\chromedriver.exe")
    def test_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_link_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.USER_PASSWORD)
        assert self.loginPage.get_link() == "https://open.spotify.com/"