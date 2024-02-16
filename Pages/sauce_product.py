from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class production:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
    
    def product(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[@id = 'add-to-cart-sauce-labs-backpack']"))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[@id = 'add-to-cart-sauce-labs-bolt-t-shirt']"))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[@id = 'add-to-cart-sauce-labs-onesie']"))).click()
        self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        self.driver.find_element(By.XPATH, "//button[@id='checkout']").click()