from locators.dzen_page_locators import DzenPageLocators
from pages.base_page import BasePage
import allure


class DzenPageMethods(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.locators = DzenPageLocators()

    @allure.step('Ждем открытия страницы Дзена')
    def wait_for_dzen_tab_opens(self):
        return self.is_element_visible(self.locators.DZEN_LOGO)
