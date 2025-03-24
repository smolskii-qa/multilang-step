import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='choose language: es or fr')


@pytest.fixture()
def browser(request):
    options = Options()
    browser_language = request.config.getoption('language')
    if browser_language in ['es', 'fr']:
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise ValueError('empty --language option')
    yield browser
    browser.quit()
