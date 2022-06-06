import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants
from pages.start_page import StartPage
from pages.utils import User, create_driver, random_text


@pytest.mark.parametrize("browser", BaseConstants.BROWSER_LIST_UNDER_TEST)
class TestStartPage:
    @pytest.fixture(scope="function")
    def start_page(self, browser):
        driver = create_driver(browser=browser)
        yield StartPage(driver)
        driver.close()

    def test_create_post(self, signed_in_user):
        """
        - Pre-conditions:
            - Sing In/Up as a user
        - Steps:
            - Create post
            - Verify result
        """
        hello_user_page = signed_in_user
        post_create_page = hello_user_page.header.navigate_to_create_post()

        # Create a new post
        post_create_page.create_post(title=random_text(2), content=random_text(30))

        # Verify result
        post_create_page.verify_message()

    def test_create_private_post(self, signed_in_user):
        """
        - Pre-conditions:
            - SingUp as a user
            - Create post
        - Steps:
            - Create private post
            - Verify result
        """

        hello_user_page = signed_in_user
        post_create_page = hello_user_page.header.navigate_to_create_post()

        # Create a new post
        post_create_page.create_private_post(title=random_text(2), content=random_text(30))

        # Verify result
        post_create_page.verify_availability_message()
