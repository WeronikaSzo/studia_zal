from selenium.webdriver.common.by import By
from page_object_pattern.locators.locators import TestData
from page_object_pattern.pages.login_up import BasePage


class LoginPage(BasePage):

    "By locators - OR"
    EMAIL = (By.ID, "identifier")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit")
    SIGNUP_BUTTON = (By.XPATH, "/html/body/div/div/div/div/div[2]/h6/i")

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