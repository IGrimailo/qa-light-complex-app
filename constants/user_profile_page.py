class UserProfilePageConstants:
    FOLLOW_BUTTON_XPATH = './/button[contains(text(), "Follow")]'
    STOP_FOLLOW_BUTTON_XPATH = './/button[contains(text(), "Stop Following")]'
    STOP_FOLLOW_MESSAGE_XPATH = './/div[@class="alert alert-success text-center"]'
    STOP_FOLLOW_MESSAGE_TEXT = 'Successfully stopped following {username}'
    FOLLOWERS_TAB_XPATH = './/a[@href="/profile/{username}/followers"]'
    FOLLOWERS_LIST_XPATH = './/div[@class="list-group"]//a'
    FOLLOWINGS_TAB_XPATH = './/a[@href="/profile/{username}/following"]'
