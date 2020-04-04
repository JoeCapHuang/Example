import pytest
from selenium.webdriver.chrome.options import Options
from infr.driver import Driver


@pytest.fixture(autouse=True)
def _driver(request):
    options = Options()

    if 'MOBILE' in request.keywords:
        if 'ANDROID' in request.keywords:
            options.add_experimental_option('mobileEmulation', {'deviceName': 'Pixel 2'})
        elif 'IOS' in request.keywords:
            options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone 8'})

    elif 'TABLET' in request.keywords:
        if 'ANDROID' in request.keywords:
            options.add_experimental_option('mobileEmulation', {'deviceName': 'Nexus 10'})
        elif 'IOS' in request.keywords:
            options.add_experimental_option('mobileEmulation', {'deviceName': 'iPad'})

    driver = Driver(options=options)
    driver.set_window_size(1920, 1080)

    yield driver

    driver.__class__._instances = {}
    driver.quit()
