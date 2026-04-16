import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from ..pom_pages import *

# chargement de la feature
scenarios("../features/search_prices.feature")


# selenium Fixture
@pytest.fixture
# réutilisation de la fixture à travers des steps
def selenium(scope="module"):
    options = webdriver.FirefoxOptions()
    ## pas besoin de GUI !!!
    options.headless = True
    return webdriver.Remote(
        command_executor="http://selenium-server:4444/wd/hub", options=options
    )


@given(parsers.parse("I get on the home page"), target_fixture="home_page")
def get_home_page(selenium):
    selenium.get(HomePage.DAWAN_HOMEPAGE_URL)
    return HomePage(selenium)


@when(parsers.parse("I type the value {keyword} in the search input field"))
def log(home_page, keyword):
    home_page.search(keyword)


@then(parsers.parse("I see that the price is {price}"))
def check(selenium, price):
    results_page = ResultsPage(selenium)
    for check in results_page.check_prices(price):
        assert check
