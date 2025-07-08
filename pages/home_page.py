from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePageMethods(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.locators = HomePageLocators()

    def wait_for_load_home_page(self):
        return self.is_element_visible(self.locators.COOKIES_ACCEPT_BUTTON)

    def click_cookies_accept_button(self):
        self.click(self.locators.COOKIES_ACCEPT_BUTTON)

    def click_yandex_logo_button(self):
        self.click(self.locators.YANDEX_LOGO_BUTTON)

    def click_scooter_logo_button(self):
        self.click(self.locators.SCOOTER_LOGO_BUTTON)

    def click_header_order_button(self):
        self.click(self.locators.HEADER_ORDER_BUTTON)

    def click_bottom_order_button(self):
        self.click(self.locators.BOTTOM_ORDER_BUTTON)

    def click_faq_question(self,by_locator):
        self.click(by_locator)

    def text_answer_for_question(self,by_locator):
        return self.get_text(by_locator)
