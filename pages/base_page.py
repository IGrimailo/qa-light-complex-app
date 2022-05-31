class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def fill_field(self):
        """Send data into the field"""
        # - Find element
        login_field = driver.find_element(by=By.XPATH, value='.//input[@placeholder="Username"]')
        # - Clear field
        login_field.clear()
        # - Fill field
        login_field.send_keys("Irina")
