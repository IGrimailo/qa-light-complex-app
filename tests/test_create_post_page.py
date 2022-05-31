import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants
from pages.start_page import StartPage
from pages.utils import User


class TestCreatePostPage:
    @pytest.fixture(scope="function")
    def start_page(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(1)
        driver.get(BaseConstants.BASE_URL)
        yield StartPage(driver)
        driver.close()

    @pytest.fixture(scope="function")
    def random_user(self):
        return User()

    @pytest.fixture(scope="function")
    def signed_in_user(self, start_page, random_user):
        start_page.sign_up(username=random_user.username, email=random_user.email, password=random_user.password)
        hello_user_page = start_page.click_sign_up_and_verify()
        return hello_user_page, random_user

    def test_create_post(self, signed_in_user):
        """
        - Pre-conditions:
            - Sing In/Up as a user
        - Steps:
            - Create post
            - Verify result
        """
        hello_user_page, user = signed_in_user
        post_create_page = hello_user_page.header.navigate_to_create_post()

        # Create a new post
        post_create_page.create_post(title="Test new post", content="Test new content")

        # Verify result
        post_create_page.verify_message()
