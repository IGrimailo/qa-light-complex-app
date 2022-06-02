import pytest

from constants.base import BaseConstants
from pages.start_page import StartPage
from pages.utils import create_driver, User, random_text


@pytest.mark.parametrize("browser", BaseConstants.BROWSER_LIST_UNDER_TEST)
class TestUserProfilePage:

    @pytest.fixture(scope="function")
    def start_page(self, browser):
        driver = create_driver(browser=browser)
        yield StartPage(driver)
        driver.close()

    @pytest.fixture(scope="function")
    def user_with_post(self, start_page):
        user = User()
        user.fill_properties()
        # Sign Up
        start_page.sign_up(username=user.username, email=user.email, password=user.password)
        hello_user_page = start_page.click_sign_up_and_verify()
        # Create a new post
        post_create_page = hello_user_page.header.navigate_to_create_post()
        title = random_text(2)
        post_create_page.create_post(title=title, content=random_text(30))
        user.posts.append(title)
        post_create_page.header.logout()
        return user

    def test_follow_user(self, user_with_post, signed_in_user, random_user):
        """
        - Pre-condition:
            - Create user 1
            - Add post for user 1
            - Create user 2
        - Steps:
            - Search for user`s 1 post on user 2
            - Move to post page
            - Move to user 1 page
            - Follow user 1 as user 2
            - Verify user 1 followers
            - Move to user 2 profile
            - Verify user 2 followings
        """
        hello_user_page = signed_in_user

        # Search
        post_page = hello_user_page.header.navigate_to_post_by_title(user_with_post.posts[0])

        # Move to post page
        user_profile_page = post_page.navigate_to_user_profile(user_with_post.username)

        # Move to user 1 page
        # Follow user 1 as user 2
        user_profile_page.follow_user_and_verify(user_with_post.username, random_user.username)

        # Move to user2 profile
        user_profile_page.header.navigate_to_profile(random_user.username)

        # Verify user2 followings
        user_profile_page.verify_followings(random_user.username, user_with_post.username)

    def test_stop_follow_user(self, user_with_post, signed_in_user, random_user):
        """
        - Pre-condition:
            - Create user 1
            - Add post for user 1
            - Create user 2
        - Steps:
            - Search for user`s 1 post on user 2
            - Move to post page
            - Move to user 1 page
            - Follow user 1 as user 2
            - Verify user 1 followers
            - Stop follow user 1
            - Move to user 2 profile
            - Verify user 2 followings
        """
        hello_user_page = signed_in_user

        # Search
        post_page = hello_user_page.header.navigate_to_post_by_title(user_with_post.posts[0])

        # Move to post page
        user_profile_page = post_page.navigate_to_user_profile(user_with_post.username)

        # Move to user 1 page
        # Follow user 1 as user 2
        user_profile_page.follow_user_and_verify(user_with_post.username, random_user.username)

        # Stop follow user 1
        user_profile_page.stop_follow_user_and_verify(user_with_post.username, random_user.username)

        # Move to user2 profile
        user_profile_page.header.navigate_to_profile(random_user.username)

        # Verify user2 followings
        user_profile_page.verify_no_followings(random_user.username, user_with_post.username)
