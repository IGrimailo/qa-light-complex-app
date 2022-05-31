import datetime
import logging
import time
from time import sleep


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
        current_datetime = int(time.time())

        self.username = username if username else f'Irina{current_datetime}'
        self.email = email if email else f'test{current_datetime}@gmail.com'
        self.password = password if password else f'password{current_datetime}'
