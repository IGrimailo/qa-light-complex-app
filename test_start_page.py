import logging
import time

from time import sleep

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
        driver.get(BaseConstants.BASE_URL)
        yield StartPage(driver)
        driver.close()

    @pytest.fixture(scope="function")
    def random_user(self):
        return User()

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
        self.log.info("Invalid user tried to signed in")
        start_page.sign_in(username=random_user.username, password=random_user.password)
        sleep(2)

        # Verify error message
        self.log.info("Verifying error message")
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
        self.log.info("Empty user tried to signed in")
        start_page.sign_in()

        # Verify error message
        self.log.info("Verifying error message")
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
        self.log.info('New user registration')
        start_page.sign_up(username=random_user.username, email=random_user.email, password=random_user.password)
        sleep(2)

        # Verify success registration
        self.log.info('Verifying success registration')
        start_page.verify_success_sign_up(username=random_user.username)

    def test_user_already_exists(self, start_page, random_user):
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
        self.log.info('Registering a user with an existing email')
        start_page.sign_up(username=random_user.username, email=random_user.email, password=random_user.password)
        sleep(2)

        # Verify success registration
        self.log.info('Verifying error message')
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

        self.log.info('Registering a user with an invalid email')
        start_page.sign_up(username=random_user.username, email=email, password=random_user.password)
        sleep(2)

        # Verify success registration
        self.log.info('Verifying error message')
        start_page.verify_error_message_sing_up()
