from selenium.webdriver import ActionChains
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.wait import WebDriverWait
from settings import WAIT_TIME


class WebElement(webelement.WebElement):

    def __init__(self, webelement):
        from infr.driver import Driver
        super().__init__(parent=webelement._parent, id_=webelement._id, w3c=webelement._w3c)
        self._driver = Driver()
        self._selenium_element = webelement

    def __getitem__(self, item):
        return self._selenium_element.get_attribute(item)

    def get_element(self, locator, wait_time=WAIT_TIME):
        element = WebDriverWait(self, wait_time).until(
            lambda x: self.find_element(locator.by, locator.value)
        )
        return WebElement(element)

    def get_elements(self, locator, wait_time=WAIT_TIME):
        elements = WebDriverWait(self, wait_time).until(
            lambda x: self.find_elements(locator.by, locator.value)
        )
        return [WebElement(element) for element in elements]

    def hover_over(self):
        hover = ActionChains(self._driver).move_to_element(self)
        hover.perform()
