import pytest
from selene import browser, be, have


@pytest.fixture()
def size_window(scope='function', autouse=True):
    browser.config.driver_name = 'chrome'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()