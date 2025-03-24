import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import browser

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_if_add_to_basket_button_exists(browser):
    browser.get(url)
    add_to_basket_button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn-add-to-basket')))
    assert add_to_basket_button is not None, '"Add to basket" button wasn\'t found'
    # time.sleep(30)
