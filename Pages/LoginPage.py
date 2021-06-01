from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage

class LoginPage(BasePage):

    "By locators - OR"
    EMAIL = (By.ID, "login-username")
    PASSWORD = (By.ID, "login-password")
    LOGIN_BUTTON = (By.ID, "login-button")
    SIGNUP_BUTTON = (By.ID, "sign-up-link")

    "constructor of the page class"
    def __init__(self, driver):
        super().__init__(driver)
        driver.get(TestData.BASE_URL)

    "Page Actions"
    def get_login_page_title(self, title):
        return self.get_title(title)

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_BUTTON)

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)





