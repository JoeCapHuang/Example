from infr.basepage import BasePage
from infr.locator import (
    Button,
    TextInput,
    Locator,
)
from selenium.webdriver.common.by import By
from hamcrest import *


class CatalogPageDNS(BasePage):
    city_choose = Button(By.XPATH, '//div[@class="city-select w-choose-city-widget"]')

    find_city = TextInput(By.XPATH, '//input[@data-role="search-city"]')

    selected_city = Button(By.XPATH, '//span[not (text()) and ./mark[text() = "Челябинск"]]')

    selected_filter = Locator(By.XPATH, '//span[@class="top-filter__selected"]')

    item_price = Locator(By.XPATH, '//div[@class="product-price__current"]')

    buy_button = Button(By.XPATH, '//div[@class="primary-btn"]')

    basket_price = Locator(By.XPATH, '//span[@class="cart-link__price"]')

    def check_price(self):
        items = self.item_price().get_all_elements()
        first_item_price = items[0].text
        reference_price = int(first_item_price.replace(' ', ''))
        for item in items[1:]:
            price = int(item.text.replace(' ', ''))
            assert_that(reference_price, less_than_or_equal_to(price))
