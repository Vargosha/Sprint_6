from locators.dzen_page_locators import DzenPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class DzenPageMethods:
    dzen_url = 'https://dzen.ru/?yredirect=true'

    def __init__(self,driver):
        self.driver = driver
        self.locators = DzenPageLocators()

    def wait_for_dzen_tab_opens(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.locators.DZEN_LOGO))
