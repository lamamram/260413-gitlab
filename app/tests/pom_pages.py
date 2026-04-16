from selenium.webdriver.common.by import By
import re


class Page:
    DAWAN_HOMEPAGE_URL = "https://www.dawan.fr"

    def __init__(self, driver) -> None:
        self.driver = driver


class HomePage(Page):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.input_search = self.driver.find_element(By.ID, "motsclefs")
        self.btn_submit = self.driver.find_element(By.ID, "search-btn")

    def search(self, keyword):
        # éditer les champs "motsclefs"
        self.input_search.send_keys(keyword)
        self.btn_submit.click()


class ResultsPage(Page):
    def __init__(self, driver):
        super().__init__(driver=driver)
        self.paragraphs = driver.find_elements(
            By.XPATH, "/html/body/section/main/section//p"
        )

    def check_prices(self, price):
        checks = []
        for p in self.paragraphs:
            if m := re.search(r" [0-9 ]+ €", p.text):
                checks.append(m.group(0) == price + " €")
        return checks
