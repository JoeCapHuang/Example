from infr.basepage import BasePage
from infr.locator import (
    Button,
    Locator,
)
from selenium.webdriver.common.by import By


class MainPageDNS(BasePage):
    url = 'https://www.dns-shop.ru/'

    basket = Locator(By.XPATH, '//span[@class="cart-link__lbl"]')

    menu_root = Button(By.XPATH, '//a[text() = "ТВ и Развлечения"]')

    sub_item_nintendo = Button(By.XPATH, '//a[text()="Nintendo"]')

    sub_item_sony = Button(By.XPATH, '//a[text()="PlayStation"]')

    sub_item_microsoft = Button(By.XPATH, '//a[text()="Microsoft Xbox"]')

    last_item_nintendo = Button(By.XPATH, '//a[text()="Консоли Nintendo"]')

    last_item_sony = Button(By.XPATH, '//a[text()="Консоли PlayStation"]')

    last_item_microsoft = Button(By.XPATH, '//a[text()="Консоли Microsoft Xbox"]')
