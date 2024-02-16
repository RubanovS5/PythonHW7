from selenium.webdriver.common.by import By

class assert_color:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def color(self, name):
       green_rgba = "rgba(209, 231, 221, 1)"
       name =  self.driver.find_element(By.CSS_SELECTOR, "#first-name").value_of_css_property("background-color")
       assert name == green_rgba
