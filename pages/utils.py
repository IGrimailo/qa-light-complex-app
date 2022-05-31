import time


class User:
    current_datetime = int(time.time())

    def __init__(self, username="", email="", password=""):
        self.username = username if username else f'Irina{self.current_datetime}'
        self.email = email if email else f'test{self.current_datetime}@gmail.com'
        self.password = password if password else f'password{self.current_datetime}'
