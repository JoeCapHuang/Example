from infr.basepage import BasePage
from infr.locator import (
    Locator,
    Button,
    TextInput,
)
from selenium.webdriver.common.by import By


class GooglePages(BasePage):

    url = 'https://google.com/'

    search_field = TextInput(By.XPATH, '//div[@jscontroller]/div[@jsname]//input')

    search_button = Button(By.XPATH, '//div[@jscontroller]/div[@jsname]//input[@type ="submit"]')

    lucky_button = Button(By.XPATH, '//div[@jscontroller]/div[@jsname]//input[@jsaction="sf.lck"]')

    checked_object = Locator(By.XPATH, '//div[@jscontroller]/div[@lang]//div[@data-attrid ="title"]/span[1]')
