from pages.dns_main_page import MainPageDNS
from infr.locator import (
    Button,
    TextInput,
)
from selenium.webdriver.common.by import By


class MainPageMobileDNS(MainPageDNS):

    menu_root = Button(By.XPATH, '//span[text() = "ТВ и Развлечения"]')

    menu_sub_root = Button(By.XPATH, '//a[text() = "Игры и хобби"]')

    sub_item_nintendo = Button(By.XPATH, '//span[text()="Nintendo"]')

    sub_item_sony = Button(By.XPATH, '//span[text()="PlayStation"]')

    sub_item_microsoft = Button(By.XPATH, '//span[text()="Microsoft Xbox"]')

    last_item_nintendo = Button(By.XPATH, '//span[text()="Консоли Nintendo"]')

    last_item_sony = Button(By.XPATH, '//span[text()="Консоли PlayStation"]')

    last_item_microsoft = Button(By.XPATH, '//span[text()="Консоли Microsoft Xbox"]')

    city_choose = Button(By.XPATH, '//button[@class="button-ui button-ui_white confirm-city-mobile__choose"]')

    find_city = TextInput(By.XPATH, '//input[@data-role="search-city"]')
