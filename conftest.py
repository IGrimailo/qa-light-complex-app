import pytest

from constants.base import BaseConstants
from pages.start_page import StartPage
from pages.utils import User, create_driver


@pytest.fixture(scope="function")
def random_user():
    user = User()
    user.fill_properties()
    return user


@pytest.fixture(scope="function")
def signed_in_user(start_page, random_user):
    start_page.sign_up(username=random_user.username, email=random_user.email, password=random_user.password)
    hello_user_page = start_page.click_sign_up_and_verify()
    return hello_user_page


@pytest.fixture(scope="function")
def registered_user(start_page, random_user):
    start_page.sign_up(username=random_user.username, email=random_user.email, password=random_user.password)
    hello_user_page = start_page.click_sign_up_and_verify()
    hello_user_page.header.logout()
    return random_user


@pytest.fixture(scope="function")
def signed_out_user(signed_in_user):
    return signed_in_user.header.logout()
