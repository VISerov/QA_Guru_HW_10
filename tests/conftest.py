import pytest
from selene import browser
import os
import tests
from pathlib import Path


def path(file_name):
    return str(Path(tests.__file__).parent.joinpath(f'resourсes/{file_name}').absolute())



@pytest.fixture(scope='function', autouse=True)
def size_window():
    browser.config.driver_name = 'chrome'
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()
