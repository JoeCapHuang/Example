from infr.decorators import (
    android,
    mobile,
)
from pages.dns_mobile_main_page import *
from pages.dns_mobile_catalog_page import *
from hamcrest import *


@mobile()
@android()
def test_nintendo():
    main_page = MainPageMobileDNS().open()
    catalog_page = CatalogPageMobileDNS()

    main_page.city_choose().click()
    main_page.find_city().enter_text('Челябинск')
    main_page.refresh()

    main_page.menu_root().scroll_to()
    main_page.menu_root().click()
    main_page.menu_sub_root().click()
    main_page.sub_item_nintendo().scroll_to()
    main_page.sub_item_nintendo().click()
    main_page.last_item_nintendo().scroll_to()
    main_page.last_item_nintendo().click()

    catalog_page.filter_button().click()
    assert_that(catalog_page.selected_filter().get_text(), equal_to('по возрастанию цены'))

    catalog_page.check_price()
    catalog_page.buy_button().scroll_to()
    catalog_page.buy_button().click()
    catalog_page.basket_button().click()

    assert_that(catalog_page.basket_all_price().get_text(), equal_to(catalog_page.basket_item_price().get_text()))


@mobile()
@android()
def test_sony():
    main_page = MainPageMobileDNS().open()
    catalog_page = CatalogPageMobileDNS()

    main_page.city_choose().click()
    main_page.find_city().enter_text('Челябинск')
    main_page.refresh()

    main_page.menu_root().scroll_to()
    main_page.menu_root().click()
    main_page.menu_sub_root().click()
    main_page.sub_item_sony().scroll_to()
    main_page.sub_item_sony().click()
    main_page.last_item_sony().scroll_to()
    main_page.last_item_sony().click()

    catalog_page.filter_button().click()
    assert_that(catalog_page.selected_filter().get_text(), equal_to('по возрастанию цены'))

    catalog_page.check_price()
    catalog_page.buy_button().scroll_to()
    catalog_page.buy_button().click()
    catalog_page.basket_button().click()

    assert_that(catalog_page.basket_all_price().get_text(), equal_to(catalog_page.basket_item_price().get_text()))


@mobile()
@android()
def test_microsoft():
    main_page = MainPageMobileDNS().open()
    catalog_page = CatalogPageMobileDNS()

    main_page.city_choose().click()
    main_page.find_city().enter_text('Челябинск')
    main_page.refresh()

    main_page.menu_root().scroll_to()
    main_page.menu_root().click()
    main_page.menu_sub_root().click()
    main_page.sub_item_microsoft().scroll_to()
    main_page.sub_item_microsoft().click()
    main_page.last_item_microsoft().scroll_to()
    main_page.last_item_microsoft().click()

    catalog_page.filter_button().click()
    assert_that(catalog_page.selected_filter().get_text(), equal_to('по возрастанию цены'))

    catalog_page.check_price()
    catalog_page.buy_button().scroll_to()
    catalog_page.buy_button().click()
    catalog_page.basket_button().click()

    assert_that(catalog_page.basket_all_price().get_text(), equal_to(catalog_page.basket_item_price().get_text()))
