from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def fill_field(self, xpath, value):
        """Send data into the field"""
        field = self.driver.find_element(by=By.XPATH, value=xpath)
        field.clear()
        field.send_keys(value)

    def click(self, xpath):
        """Find and click the element"""
        self.driver.find_element(by=By.XPATH, value=xpath).click()
