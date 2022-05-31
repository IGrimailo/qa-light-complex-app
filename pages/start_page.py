from time import sleep

from selenium.webdriver.common.by import By

from constants.start_page import StartPageConstants
from pages.base_page import BasePage


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    def sign_in(self, username="", password=""):
        """Sing in using provided values"""
        self.fill_field(xpath=self.constants.SING_IN_USERNAME_XPATH, value=username)
        self.fill_field(xpath=self.constants.SING_IN_PASSWORD_XPATH, value=password)
        self.click(xpath=self.constants.SING_IN_BUTTON_XPATH)

    def verify_sign_in_error(self):
        """Verify error message"""
        error_message = self.driver.find_element(by=By.XPATH, value=self.constants.SING_IN_ERROR_MESSAGE_XPATH)
        assert error_message.text == self.constants.SING_IN_ERROR_MESSAGE_TEXT, 'Text is not valid'

    def sign_up(self, username="", email="", password=""):
        """Sing up the user using provided values"""
        self.fill_field(xpath=self.constants.SING_UP_USERNAME_XPATH, value=username)
        self.fill_field(xpath=self.constants.SING_UP_EMAIL_XPATH, value=email)
        self.fill_field(xpath=self.constants.SING_UP_PASSWORD_XPATH, value=password)
        sleep(2)
        self.click(xpath=self.constants.SING_UP_BUTTON_XPATH)

    def verify_success_sign_up(self, username):
        """Verify success message after sing up"""
        success_message = self.driver.find_element(by=By.XPATH, value=self.constants.SUCCESS_MESSAGE_XPATH)
        assert success_message.text == self.constants.SUCCESS_MESSAGE_TEXT.format(
            text=username.lower()), 'User is not registered'

    def verify_error_message_sing_up(self):
        """Verify error message after sing up with existing email"""
        error_message = self.driver.find_element(by=By.XPATH, value=self.constants.SING_UP_EMAIL_ERROR_MESSAGE_XPATH)
        assert error_message.text in self.constants.SING_UP_EMAIL_ERROR_MESSAGE_TEXT, 'User is registered'
