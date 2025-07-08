import pytest
from selenium import webdriver
from pages.home_page import HomePageMethods
from tests.urls import HOME_PAGE_URL


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture
def homepage(driver):
    homepage = HomePageMethods(driver)
    driver.get(HOME_PAGE_URL)
    homepage.wait_for_load_home_page()
    homepage.click_cookies_accept_button()
    return homepage
