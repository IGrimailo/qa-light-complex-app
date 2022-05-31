import time


class User:

    def __init__(self, username="", email="", password=""):
        current_datetime = int(time.time())

        self.username = username if username else f'Irina{current_datetime}'
        self.email = email if email else f'test{current_datetime}@gmail.com'
        self.password = password if password else f'password{current_datetime}'
