from constants.hello_user_page import HelloUserPageConstants
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import log_wrapper


class HelloUserPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HelloUserPageConstants()
        self.header = Header(driver)

    @log_wrapper
    def verify_success_sign_up(self, username):
        """Verify success message after sing up"""
        success_message = self.wait_until_displayed(xpath=self.constants.SUCCESS_MESSAGE_XPATH)
        assert success_message.text == self.constants.SUCCESS_MESSAGE_TEXT.format(
            username=username.lower()), 'User is not registered'
