import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import FirefoxProfile


def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default='ru',
                     help="Choose language: en, fr, ...")
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options_chrome = Options()
        options_chrome.add_argument("--lang={}".format(user_language))
        browser = webdriver.Chrome(options=options_chrome)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options_firefox = FirefoxProfile()
        options_firefox.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(firefox_profile=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser

    print("\nquit browser..")
    browser.quit()

