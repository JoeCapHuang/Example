from infr.decorators import (
    mobile,
    android,
    ios,
)
from pages.reddit_main_page import *


@mobile()
@android()
def test_android():
    reddit_main_page = RedditMainPageMobile().open()
    reddit_main_page.browser_chrome().get_text()


@mobile()
@ios()
def test_ios():
    RedditMainPageMobile().open()
    reddit_main_page = RedditMainPageMobile()
    reddit_main_page.browser_safari().get_text()
