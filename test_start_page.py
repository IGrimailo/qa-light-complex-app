import logging
import time

from time import sleep
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestStartPage:
    log = logging.getLogger('[StartPage]')
    current_datetime = int(time.time())

    def test_invalid_login(self):
        """
        - Create driver
        - Open start page
        - Fill field login
        - Fill field password
        - Click on 'Sing In' button
        - Verify error message
        """
        # Create driver
        driver = WebDriver(executable_path='/Users/grimaylo/PycharmProjects/qa-light-complex-app/chromedriver')

        # Open start page
        self.log.info("Opening start page")
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')

        # Fill field login
        self.log.info("Filling login field")
        # - Find element
        login_field = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Username"]')
        # - Clear field
        login_field.clear()
        # - Fill field
        login_field.send_keys("Irina")

        # Fill field password
        self.log.info("Filling password field")
        # - Find element
        password_field = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Password"]')
        # - Clear field
        password_field.clear()
        # - Fill field
        password_field.send_keys("123456789")

        # Click on 'Sign In' button
        self.log.info("Going to click 'Sign In' button")
        sing_in_button = driver.find_element(by=By.XPATH, value='.//button[text()="Sign In"]')
        sing_in_button.click()
        sleep(2)

        # Verify error message
        self.log.info("Verifying error message")
        error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_message.text == 'Invalid username / password', 'Text is not valid'

        # Close driver
        driver.close()

    def test_empty_fields(self):
        """
        - Create driver
        - Open start page
        - Clear field login
        - Clear field password
        - Click on 'Sing In' button
        - Verify error message
        """
        # Create driver
        driver = WebDriver(executable_path='/Users/grimaylo/PycharmProjects/qa-light-complex-app/chromedriver')

        # Open start page
        self.log.info("Opening start page")
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')

        # Fill field login
        self.log.info("Clearing login field")
        # - Find element
        login_field = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Username"]')
        # - Clear field
        login_field.clear()

        # Fill field password
        self.log.info("Clearing password field")
        # - Find element
        password_field = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Password"]')
        # - Clear field
        password_field.clear()

        # Click on 'Sign In' button
        self.log.info("Going to click 'Sign In' button")
        sing_in_button = driver.find_element(by=By.XPATH, value='.//button[text()="Sign In"]')
        sing_in_button.click()

        # Verify error message
        self.log.info("Verifying error message")
        error_message = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_message.text == 'Invalid username / password', 'Text is not valid'

        # Close driver
        driver.close()

    def test_success_registration(self):
        """
        - Create driver
        - Open start page
        - Fill field user name
        - Fill field email
        - Fill field password
        - Click on 'Sing up' button
        - Verify success registration
        """

        # Create driver
        driver = WebDriver(executable_path='/Users/grimaylo/PycharmProjects/qa-light-complex-app/chromedriver')

        # Open start page
        self.log.info("Opening start page")
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')

        # Fill field user name
        self.log.info("Filling user name field")
        # - Find element
        username_field = driver.find_element(by=By.ID, value='username-register')
        # - Clear field
        username_field.clear()
        # - Fill field
        username_field.send_keys(f'Irina{self.current_datetime}')
        sleep(1)

        # Fill field email
        self.log.info("Filling email field")
        # - Find element
        login_field = driver.find_element(by=By.ID, value='email-register')
        # - Clear field
        login_field.clear()
        # - Fill field
        login_field.send_keys(f'test{self.current_datetime}@gmail.com')
        sleep(1)

        # Fill field password
        self.log.info("Filling password field")
        # - Find element
        password_field = driver.find_element(by=By.ID, value='password-register')
        # - Clear field
        password_field.clear()
        # - Fill field
        password_field.send_keys(f'password{self.current_datetime}')
        sleep(1)

        # Click on 'Sign up' button
        self.log.info("Going to click 'Sign up for OurApp' button")
        sing_up_button = driver.find_element(by=By.XPATH, value='//*[@id="registration-form"]/button')
        sing_up_button.click()
        sleep(2)

        # Verify success registration
        self.log.info("Verifying success registration")
        success_message = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/h2')
        assert success_message.text == f'Hello irina{self.current_datetime}, your feed is empty.', 'User is not registered'

        # Close driver
        driver.close()

    def test_user_already_exists(self):
        """
        - Create driver
        - Open start page
        - Fill field user name
        - Fill field email
        - Fill field password
        - Click on 'Sing up' button
        - Verify error message
        """

        # Create driver
        driver = WebDriver(executable_path='/Users/grimaylo/PycharmProjects/qa-light-complex-app/chromedriver')

        # Open start page
        self.log.info("Opening start page")
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')

        # Fill field user name
        self.log.info("Filling user name field")
        # - Find element
        username_field = driver.find_element(by=By.ID, value='username-register')
        # - Clear field
        username_field.clear()
        # - Fill field
        username_field.send_keys(f'Irina{self.current_datetime}')
        sleep(1)

        # Fill field email
        self.log.info("Filling email field")
        # - Find element
        login_field = driver.find_element(by=By.ID, value='email-register')
        # - Clear field
        login_field.clear()
        # - Fill field
        login_field.send_keys(f'test{self.current_datetime}@gmail.com')
        sleep(1)

        # Fill field password
        self.log.info("Filling password field")
        # - Find element
        password_field = driver.find_element(by=By.ID, value='password-register')
        # - Clear field
        password_field.clear()
        # - Fill field
        password_field.send_keys(f'password{self.current_datetime}')
        sleep(1)

        # Click on 'Sign up' button
        self.log.info("Going to click 'Sign up for OurApp' button")
        sing_up_button = driver.find_element(by=By.XPATH, value='//*[@id="registration-form"]/button')
        sing_up_button.click()
        sleep(2)

        # Verify error message
        self.log.info("Verifying error message")
        error_message = driver.find_element(by=By.XPATH, value='//*[@id="registration-form"]/div[2]/div')
        assert error_message.text == 'That email is already being used.', 'User is registered'

        # Close driver
        driver.close()

    def test_invalid_email(self):
        """
        - Create driver
        - Open start page
        - Fill field user name
        - Fill field email
        - Fill field password
        - Click on 'Sing up' button
        - Verify error message
        """

        # Create driver
        driver = WebDriver(executable_path='/Users/grimaylo/PycharmProjects/qa-light-complex-app/chromedriver')

        # Open start page
        self.log.info("Opening start page")
        driver.get('https://qa-complex-app-for-testing.herokuapp.com/')

        # Fill field user name
        self.log.info("Filling user name field")
        # - Find element
        username_field = driver.find_element(by=By.ID, value='username-register')
        # - Clear field
        username_field.clear()
        # - Fill field
        username_field.send_keys(f'Irina{self.current_datetime}')
        sleep(1)

        # Fill field email
        self.log.info("Filling email field")
        # - Find element
        login_field = driver.find_element(by=By.ID, value='email-register')
        # - Clear field
        login_field.clear()
        # - Fill field
        login_field.send_keys(f'test{self.current_datetime}')
        sleep(1)

        # Fill field password
        self.log.info("Filling password field")
        # - Find element
        password_field = driver.find_element(by=By.ID, value='password-register')
        # - Clear field
        password_field.clear()
        # - Fill field
        password_field.send_keys(f'password{self.current_datetime}')
        sleep(1)

        # Click on 'Sign up' button
        self.log.info("Going to click 'Sign up for OurApp' button")
        sing_up_button = driver.find_element(by=By.XPATH, value='//*[@id="registration-form"]/button')
        sing_up_button.click()
        sleep(2)

        # Verify error message
        self.log.info("Verifying error message")
        error_message = driver.find_element(by=By.XPATH, value='//*[@id="registration-form"]/div[2]/div')
        assert error_message.text == 'You must provide a valid email address.', 'User is registered'

        # Close driver
        driver.close()
