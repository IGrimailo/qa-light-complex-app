from constants.create_post_page import CreatePostPageConstants
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import log_wrapper


class CreatePostPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CreatePostPageConstants()
        self.header = Header(driver)

    @log_wrapper
    def create_post(self, title: str, content: str) -> None:
        """Create a new post using provided values"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=title)
        self.fill_field(xpath=self.constants.BODY_CONTENT_FIELD_XPATH, value=content)
        self.click(xpath=self.constants.SAVE_POST_BUTTON_XPATH)

    @log_wrapper
    def create_private_post(self, title: str, content: str) -> None:
        """Create a new post using provided values"""
        self.fill_field(xpath=self.constants.TITLE_FIELD_XPATH, value=title)
        self.fill_field(xpath=self.constants.BODY_CONTENT_FIELD_XPATH, value=content)
        self.click(xpath=self.constants.SELECT_VALUE_XPATH.format(type='One Person'))
        self.click(xpath=self.constants.SAVE_POST_BUTTON_XPATH)

    @log_wrapper
    def verify_message(self) -> None:
        """Verify success message after create a new post"""
        success_message = self.wait_until_displayed(xpath=self.constants.POST_CREATE_SUCCESS_MESSAGE_XPATH)
        assert success_message.text == self.constants.POST_CREATE_SUCCESS_MESSAGE_TEXT, 'Post is not created'

    @log_wrapper
    def verify_availability_message(self) -> None:
        """Verify success message after create a new post"""
        success_message = self.wait_until_displayed(xpath=self.constants.TYPE_AVAILABILITY_XPATH)
        assert success_message.text == self.constants.TYPES_OF_AVAILABILITY[1], 'Post is not created'
