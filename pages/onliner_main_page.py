from infr.basepage import BasePage
from infr.locator import Locator
from selenium.webdriver.common.by import By
from hamcrest import *
from infr.api import get_onliner_forecast


class OnlinerMainPage(BasePage):
    url = 'https://www.onliner.by/'

    temperature = Locator(By.XPATH, '//a[@class ="b-top-navigation-informers__link" and ./i]/span')

    def check_temperature(self):
        api_temperature = get_onliner_forecast()
        page_temperature = self.temperature().get_text().replace('°', '')
        assert_that(page_temperature, equal_to(api_temperature['now']['temperature']))
