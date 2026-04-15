import pytest
from selenium.webdriver.common.by import By
import re

@pytest.mark.e2e
def test_dawan_prices(selenium):
    # chercher la page https://www.dawan.fr 
    DAWAN_HOMEPAGE_URL = "https://www.dawan.fr"
    selenium.get(DAWAN_HOMEPAGE_URL)
    
    search_input = selenium.find_element(By.ID, "motsclefs")
    search_input.send_keys("selenium")
    search_btn = selenium.find_element(By.ID, "search-btn")
    search_btn.click()

    # transition dans la page de résultats

    paragraphs = selenium.find_elements(By.XPATH, "/html/body/section/main/section//p")
    prices = []
    for p in paragraphs:
        if (m:=re.search(r" [0-9 ]+ €", p.text)):
            assert m.group(0) == " 1 432 €"