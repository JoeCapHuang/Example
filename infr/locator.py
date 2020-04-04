from infr.driver import Driver
from selenium.webdriver.remote.webelement import WebElement
from settings import WAIT_TIME


class Locator:
    driver = None
    element: 'WebElement' = None

    def __init__(self, by, value):
        self.by = by
        self.value = value

    def __call__(self, wait_time=WAIT_TIME):
        self.driver = Driver()
        self.element = self.driver.get_element(self, wait_time=wait_time)
        return self

    def get_all_elements(self):
        return self.element.get_elements(self)

    def find_elements(self):
        return self.get_all_elements()

    def get_text(self):
        return self.element.text

    def hover(self):
        self.element.hover_over()

    def scroll_to(self):
        return self.element.location_once_scrolled_into_view

    def click(self):
        self.element.click()


class Button(Locator):
    ...


class TextInput(Locator):

    def enter_text(self, text):
        self.element.send_keys(text)
