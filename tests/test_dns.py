from pages.dns_main_page import *
from pages.dns_catalog_page import *
from hamcrest import *


def test_nintendo():
    main_page = MainPageDNS().open()
    catalog_page = CatalogPageDNS()

    main_page.menu_root().hover()
    main_page.sub_item_nintendo().hover()
    main_page.last_item_nintendo().click()

    catalog_page.city_choose().click()
    catalog_page.find_city().enter_text('Челябинск')
    catalog_page.selected_city().click()
    catalog_page.refresh()

    assert_that(catalog_page.selected_filter().get_text(), equal_to('по возрастанию цены'))
    catalog_page.check_price()
    catalog_page.buy_button().click()
    assert_that(catalog_page.basket_price().get_text(), equal_to(catalog_page.item_price().get_text()))


def test_sony():
    main_page = MainPageDNS().open()
    catalog_page = CatalogPageDNS()

    main_page.menu_root().hover()
    main_page.sub_item_sony().hover()
    main_page.last_item_sony().click()

    catalog_page.city_choose().click()
    catalog_page.find_city().enter_text('Челябинск')
    catalog_page.selected_city().click()
    catalog_page.refresh()

    assert_that(catalog_page.selected_filter().get_text(), equal_to('по возрастанию цены'))
    catalog_page.check_price()
    catalog_page.buy_button().click()
    assert_that(catalog_page.basket_price().get_text(), equal_to(catalog_page.item_price().get_text()))


def test_microsoft():
    main_page = MainPageDNS().open()
    catalog_page = CatalogPageDNS()

    main_page.menu_root().hover()
    main_page.sub_item_microsoft().hover()
    main_page.last_item_microsoft().click()

    catalog_page.city_choose().click()
    catalog_page.find_city().enter_text('Челябинск')
    catalog_page.selected_city().click()
    catalog_page.refresh()

    assert_that(catalog_page.selected_filter().get_text(), equal_to('по возрастанию цены'))
    catalog_page.check_price()
    catalog_page.buy_button().click()
    assert_that(catalog_page.basket_price().get_text(), equal_to(catalog_page.item_price().get_text()))
