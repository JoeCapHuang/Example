from infr.basepage import BasePage
from infr.locator import Locator
from selenium.webdriver.common.by import By


class RedditMainPageMobile(BasePage):
    url = 'https://www.reddit.com/'

    browser_chrome = Locator(By.XPATH, '//span[text() = "Chrome"]')

    browser_safari = Locator(By.XPATH, '//span[text() = "Safari"]')

