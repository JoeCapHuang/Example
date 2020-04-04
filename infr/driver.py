from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from settings import (
    DRIVER_PATH,
    WAIT_TIME,
)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Driver(Chrome, metaclass=Singleton):
    from infr.webelement import WebElement

    def __init__(self, *args, **kwargs):
        super().__init__(executable_path=DRIVER_PATH, *args, **kwargs)

    def get_element(self, locator, wait_time=WAIT_TIME):
        element = WebDriverWait(self, wait_time).until(
            lambda x: self.find_element(locator.by, locator.value)
        )
        return self.WebElement(element)

    def get_elements(self, locator):
        elements = self.find_elements(locator.by, locator.value)
        return elements
