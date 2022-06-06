from constants.header import HeaderConstants
from pages.base_page import BasePage
from pages.utils import log_wrapper


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = HeaderConstants()

    @log_wrapper
    def logout(self):
        """Sing out user"""
        self.click(xpath=self.constants.SING_OUT_BUTTON_XPATH)
        from pages.start_page import StartPage
        return StartPage(self.driver)

    @log_wrapper
    def navigate_to_create_post(self):
        """Navigate to create a new post"""
        self.click(self.constants.CREATE_POST_BUTTON_XPATH)
        from pages.create_post_page import CreatePostPage
        return CreatePostPage(self.driver)

    @log_wrapper
    def navigate_to_post_by_title(self, title: str):
        """Open to the post"""
        self.click(self.constants.SEARCH_ICON_XPATH)
        self.fill_field(self.constants.SEARCH_INPUT_FIELD_XPATH, title)
        self.click(self.constants.SEARCH_RESULT_XPATH.format(title=title))
        from pages.post_page import PostPage
        return PostPage(self.driver)

    @log_wrapper
    def navigate_to_profile(self, username: str):
        """Open user profile"""
        self.click(self.constants.MY_PROFILE_BUTTON_XPATH.format(username=username.lower()))
        from pages.user_profile_page import UserProfilePage
        return UserProfilePage(self.driver)

    @log_wrapper
    def open_chat(self):
        """Open chat"""
        self.click(self.constants.CHAT_BUTTON_XPATH)
