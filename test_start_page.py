import logging
import time

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants
from pages.start_page import StartPage
from pages.utils import User


class TestStartPage:
    log = logging.getLogger('[StartPage]')
    current_datetime = int(time.time())

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
    def registered_user(self, start_page, random_user):
        start_page.sign_up(username=random_user.username, email=random_user.email, password=random_user.password)
        start_page.click_sign_up_and_verify()
        start_page.logout()
        return random_user

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
        start_page.sign_in(username=random_user.username, password=random_user.password)

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
        start_page.sign_in()

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
        start_page.click_sign_up_and_verify()

        # Verify success registration
        start_page.verify_success_sign_up(username=random_user.username)

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
        start_page.sign_in(username=registered_user.username, password=registered_user.password)

        # Verify success sign in
        start_page.verify_success_sign_up(username=registered_user.username)
