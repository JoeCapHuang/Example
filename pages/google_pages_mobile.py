from infr.locator import (
    TextInput,
    Button,
    Locator,
)
from pages.google_pages import GooglePages
from selenium.webdriver.common.by import By


class GooglePagesMobile(GooglePages):

    search_field = TextInput(By.XPATH,  '//input[@type = "search"]')

    search_button = Button(By.XPATH, '//button[@aria-label="Поиск в Google"]')

    checked_object = Locator(By.XPATH, '//span[@role = "heading"]')
