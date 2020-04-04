from pages.dns_catalog_page import CatalogPageDNS
from infr.locator import (
    Button,
    Locator,
)
from selenium.webdriver.common.by import By


class CatalogPageMobileDNS(CatalogPageDNS):

    filter_button = Button(By.XPATH, '//button[@data-role="sort-filter-btn"]')

    selected_filter = Locator(By.XPATH, '//span[@class="top-filter__selected"]')

    item_price = Locator(By.XPATH, '//div[@class="product-price__current"]')

    buy_button = Button(By.XPATH, '//div[@class="primary-btn"]')

    basket_button = Button(By.XPATH, '//div[@class="primary-btn"]/button[text() ="В корзине"]')

    basket_item_price = Locator(By.XPATH, '//span[@class="price__current"]')

    basket_all_price = Locator(By.XPATH, '//div[@class= "total-amount"]//span[@class="price__current"]')
