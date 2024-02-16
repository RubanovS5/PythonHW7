from selenium import webdriver
import pytest
from Pages.find_element_input import input_field
from Pages.assert_color import assert_color

def test_types():
    browser = webdriver.Chrome()
    data_types = input_field(browser)
    color = assert_color
    data_types.first_name("Иван")
    data_types.last_name("Петров")
    data_types.address("Ленина, 55-3")
    data_types.zip_code("")
    data_types.city("Москва")
    data_types.country("Россия")
    data_types.mail("test@skypro.com")
    data_types.phone("+7985899998787")
    data_types.job("QA")
    data_types.company("SkyPro")
    data_types.button()
    color
   


  