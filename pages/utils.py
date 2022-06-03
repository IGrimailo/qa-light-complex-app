import datetime
import logging
import time
import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as MozilaDriver

from constants.base import BaseConstants
from constants.text_for_post import EN_TEXT


def wait_until_ok(timeout=5, period=0.25):
    """Retries function until ok"""
    logger = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):

        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        logger.warning(f"Catch: {err}")
                        raise err
                    sleep(period)

        return wrapper

    return decorator


def log_wrapper(func):
    """Add log for method using doc string"""

    def wrapper(*args, **kwargs):
        log = logging.getLogger("[LogDecorator]")
        result = func(*args, **kwargs)
        log.info(f'{func.__doc__}')
        return result

    return wrapper


class User:

    def __init__(self, username="", email="", password=""):
        self.username = username
        self.email = email
        self.password = password
        self.posts = []

    def fill_properties(self):
        """Create a random user"""
        current_datetime = int(time.time())
        self.username = f'Irina{current_datetime}'
        self.email = f'test{current_datetime}@gmail.com'
        self.password = f'password{current_datetime}'


def create_driver(browser):
    """Create driver according to provided browser"""
    if browser == BaseConstants.CHROME:
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        driver = ChromeDriver(options=options)
    elif browser == BaseConstants.FIREFOX:
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        driver = MozilaDriver(options=options)
    else:
        raise ValueError(f"Unknown browser name: {browser}")
    driver.implicitly_wait(1)
    driver.get(BaseConstants.BASE_URL)
    return driver


def random_text(length=15, preset=EN_TEXT):
    """Create text for post"""
    words = preset.split(" ")
    return ' '.join(random.choice(words) for _ in range(length))
