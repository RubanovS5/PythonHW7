from selenium import webdriver
import pytest
from Pages.sauce_login import login
from Pages.sauce_product import production
from Pages.sauce_personal import my_personal
from Pages.sauce_result import summa


def test_sauce():
    browser = webdriver.Chrome()
    log = login(browser)
    prod = production(browser)
    personal = my_personal(browser)
    result = summa(browser)
    log.text("standard_user")
    log.password("secret_sauce")
    log.click()
    prod.product()
    personal.first_name("Александр")
    personal.last_name("Рубанов")
    personal.postal("196784")
    personal.click()
    result.otvet()


