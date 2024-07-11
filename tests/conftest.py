import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: es or fr")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.set_preference("intl.accept_languages", language)
    browser = webdriver.Firefox(options=options)
    yield browser
    browser.quit()
