from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class summa:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")


    def otvet(self):
        summa = WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located((By.XPATH, "//div[@class='summary_info_label summary_total_label']"))).text
        print(summa)
        self.driver.quit()

        total = 'Total: $58.29'
        if total == summa:
            print("Итоговая сумма соответсвует ожидаемой")
        else:
            print("Итоговая сумма не соответсвует ожидаемой")