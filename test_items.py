import time

from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket(browser):
    browser.get(link)
    button_basket = browser.find_elements(By.CSS_SELECTOR, "#add_to_basket_form>button")
    print(len(button_basket))
    time.sleep(11)
    assert len(button_basket) > 0, f'The basket button was not found on the page!!!'


# pytest --language=fr --browser_name=firefox test_items.py
# pytest --language=en --browser_name=chrome test_items.py