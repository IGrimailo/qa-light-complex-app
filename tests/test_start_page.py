import logging
import time

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants
from pages.start_page import StartPage
from pages.utils import User, create_driver


@pytest.mark.parametrize("browser", BaseConstants.BROWSER_LIST_UNDER_TEST)
class TestStartPage:
    current_datetime = int(time.time())

    @pytest.fixture(scope="function")
    def start_page(self, browser):
        driver = create_driver(browser=browser)
        yield StartPage(driver)
        driver.close()

    def test_invalid_login(self, start_page, random_user):
        """
        - Pre-condition:
            - Create driver
            - Open start page
        - Steps:
            - Fill field login
            - Fill field password
            - Click on 'Sing In' button
            - Verify error message
        """

        # Fill field login
        # Fill field password
        # Click on 'Sing In' button
        start_page.sign_in(random_user)

        # Verify error message
        start_page.verify_sign_in_error()

    def test_empty_fields(self, start_page):
        """
        - Pre-condition:
            - Create driver
            - Open start page
        - Steps:
            - Clear field login
            - Clear field password
            - Click on 'Sing In' button
            - Verify error message
        """

        # Clear field login
        # Clear field password
        # Click on 'Sing In' button
        start_page.sign_in(User())

        # Verify error message
        start_page.verify_sign_in_error()

    def test_success_registration(self, start_page, random_user):
        """
        - Pre-condition:
            - Create driver
            - Open start page
        - Steps:
            - Fill field user name
            - Fill field email
            - Fill field password
            - Click on 'Sing up' button
            - Verify success registration
        """

        # Fill fields login, email, password
        # Click on 'Sing Un' button
        start_page.sign_up(username=random_user.username, email=random_user.email, password=random_user.password)
        hello_user_page = start_page.click_sign_up_and_verify()

        # Verify success registration
        hello_user_page.verify_success_sign_up(username=random_user.username)

    def test_user_already_exists(self, start_page, registered_user, random_user):
        """
        - Pre-condition:
            - Create driver
            - Open start page
            - Sign up as a user
            - Logout
        - Steps:
            - Fill field username as a user
            - Fill field email as the email
            - Fill field password as a password
            - Click on 'Sing up' button
            - Verify error message
        """

        # Fill fields login, email, password
        # Click on 'Sing Un' button
        start_page.sign_up(username=random_user.username, email=registered_user.email, password=random_user.password)

        # Verify success registration
        start_page.verify_error_message_sing_up()

    def test_invalid_email(self, start_page, random_user):
        """
        - Pre-condition:
            - Create driver
            - Open start page
        - Steps:
            - Fill field user name
            - Fill field email
            - Fill field password
            - Click on 'Sing up' button
            - Verify error message
        """

        # Fill fields login, email, password
        # Click on 'Sing Un' button
        email = f'test{self.current_datetime}'

        start_page.sign_up(username=random_user.username, email=email, password=random_user.password)

        # Verify success registration
        start_page.verify_error_message_sing_up()

    def test_sign_in(self, start_page, registered_user):
        """
        - Pre-condition:
            - Sign up as a user
            - Logout
        - Steps:
            - Sign in as the user
            - Verify success sign in
        """

        # Sign in as the user
        hello_user_page = start_page.sign_in(registered_user)

        # Verify success sign in
        hello_user_page.verify_success_sign_up(username=registered_user.username)
