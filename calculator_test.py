from Pages.numbers_calculator import numbers
from selenium import webdriver
import pytest


def test_form():
    browser = webdriver.Chrome()
    calculator = numbers(browser)
    calculator.id_delay('45')
    calculator.number()
    calculator.result()


