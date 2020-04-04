from pages.onliner_main_page import *


def test_forecast():
    onliner_main_page = OnlinerMainPage().open()
    onliner_main_page.check_temperature()
