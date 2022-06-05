class CreatePostPageConstants:
    TITLE_FIELD_XPATH = '//*[@id="post-title"]'
    BODY_CONTENT_FIELD_XPATH = '//*[@id="post-body"]'
    SAVE_POST_BUTTON_XPATH = './/button[text()="Save New Post"]'
    UPDATE_POST_BUTTON_XPATH = './/button[text()="Save Updates"]'
    POST_CREATE_SUCCESS_MESSAGE_XPATH = './/div[@class="alert alert-success text-center"]'
    POST_CREATE_SUCCESS_MESSAGE_TEXT = 'New post successfully created.'
    TYPE_AVAILABILITY_XPATH = './/u'
    TYPES_OF_AVAILABILITY = ["All Users", "One Person", "Group Message"]
    SELECT_VALUE_XPATH = './/select/option[@value="{type}"]'
