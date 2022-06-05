import datetime
import os

import pytest

from constants.base import BaseConstants
from pages.hello_user_page import HelloUserPage
from pages.start_page import StartPage
from pages.utils import User, create_driver


# pylint: disable=unused-argument
def pytest_sessionstart(session):
    os.environ["PATH"] = os.environ["PATH"] + f":{os.path.abspath(BaseConstants.DRIVERS_PATH)}"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Preserve screenshot on fail"""
    outcome = yield
    result = outcome.get_result()

    if result.failed:
        driver = [item.funcargs[arg] for arg in item.funcargs if arg.endswith("_page")][0].driver
        file_name = f"{item.name}_{datetime.datetime.today().strftime('%Y-%m-%d_%H:%M:%S')}.png"
        file_path = "/Users/grimaylo/PycharmProjects/qa-light-complex-app/screenshots"
        driver.save_screenshot(os.path.join(file_path, file_name))


@pytest.fixture(scope="function")
def random_user() -> User:
    user = User()
    user.fill_properties()
    return user


@pytest.fixture(scope="function")
def signed_in_user(start_page, random_user) -> HelloUserPage:
    start_page.sign_up(username=random_user.username, email=random_user.email, password=random_user.password)
    hello_user_page = start_page.click_sign_up_and_verify()
    return hello_user_page


@pytest.fixture(scope="function")
def registered_user(start_page, random_user) -> User:
    start_page.sign_up(username=random_user.username, email=random_user.email, password=random_user.password)
    hello_user_page = start_page.click_sign_up_and_verify()
    hello_user_page.header.logout()
    return random_user


@pytest.fixture(scope="function")
def signed_out_user(signed_in_user) -> StartPage:
    return signed_in_user.header.logout()
