class StartPageConstants:
    # SING IN
    SING_IN_USERNAME_XPATH = './/input[@placeholder="Username"]'
    SING_IN_PASSWORD_XPATH = './/input[@placeholder="Password"]'
    SING_IN_BUTTON_XPATH = './/button[text()="Sign In"]'
    SING_IN_ERROR_MESSAGE_XPATH = ".//div[@class='alert alert-danger text-center']"
    SING_IN_ERROR_MESSAGE_TEXT = 'Invalid username / pasword'

    # SING UP
    SING_UP_USERNAME_XPATH = 'username-register'
    SING_UP_EMAIL_XPATH = 'email-register'
    SING_UP_PASSWORD_XPATH = 'password-register'
    SING_UP_BUTTON_XPATH = '//*[@id="registration-form"]/button'
    SING_UP_EMAIL_ERROR_MESSAGE_XPATH = '//*[@id="registration-form"]/div[2]/div'
    SING_UP_EMAIL_ERROR_MESSAGE_TEXT = ['That email is already being used.', 'You must provide a valid email address.']

    # Profile page
    SUCCESS_MESSAGE_XPATH = '/html/body/div[2]/div/h2'
    SUCCESS_MESSAGE_TEXT = 'Hello irina{text}, your feed is empty.'
