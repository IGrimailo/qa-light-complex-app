from constants.start_page import StartPageConstants
from pages.base_page import BasePage
from pages.hello_user_page import HelloUserPage
from pages.utils import log_wrapper, wait_until_ok, User


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    @log_wrapper
    def sign_in(self, user: User) -> HelloUserPage:
        """Sing in using provided values"""
        self.fill_field(xpath=self.constants.SING_IN_USERNAME_XPATH, value=user.username)
        self.fill_field(xpath=self.constants.SING_IN_PASSWORD_XPATH, value=user.password)
        self.click(xpath=self.constants.SING_IN_BUTTON_XPATH)
        return HelloUserPage(self.driver)

    @log_wrapper
    def verify_sign_in_error(self) -> None:
        """Verify error message"""
        error_message = self.wait_until_displayed(xpath=self.constants.SING_IN_ERROR_MESSAGE_XPATH)
        assert error_message.text == self.constants.SING_IN_ERROR_MESSAGE_TEXT, 'Text is not valid'

    @log_wrapper
    def sign_up(self, username: str, email: str, password: str) -> None:
        """Sing up the user using provided values"""
        self.fill_field(xpath=self.constants.SING_UP_USERNAME_XPATH, value=username)
        self.fill_field(xpath=self.constants.SING_UP_EMAIL_XPATH, value=email)
        self.fill_field(xpath=self.constants.SING_UP_PASSWORD_XPATH, value=password)
        # self.click_sign_up_and_verify()

    @wait_until_ok(timeout=10, period=1)
    @log_wrapper
    def click_sign_up_and_verify(self) -> HelloUserPage:
        """Click sign up and verify that button doesn't exists anymore"""
        self.click(xpath=self.constants.SING_UP_BUTTON_XPATH)
        assert not self.is_element_exists(xpath=self.constants.SING_UP_BUTTON_XPATH)
        return HelloUserPage(self.driver)

    @log_wrapper
    def verify_error_message_sing_up(self) -> None:
        """Verify error message after sing up with existing email"""
        error_message = self.wait_until_displayed(xpath=self.constants.SING_UP_EMAIL_ERROR_MESSAGE_XPATH)
        assert error_message.text in self.constants.SING_UP_EMAIL_ERROR_MESSAGE_TEXT, 'User is registered'
