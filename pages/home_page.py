from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePageMethods(BasePage):
    home_page_url = 'https://qa-scooter.praktikum-services.ru/'

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

    def click_faq_question_one(self):
        self.click(self.locators.FAQ_QUESTION_ONE)

    def click_faq_question_two(self):
        self.click(self.locators.FAQ_QUESTION_TWO)

    def click_faq_question_three(self):
        self.click(self.locators.FAQ_QUESTION_THREE)

    def click_faq_question_four(self):
        self.click(self.locators.FAQ_QUESTION_FOUR)

    def click_faq_question_five(self):
        self.click(self.locators.FAQ_QUESTION_FIVE)

    def click_faq_question_six(self):
        self.click(self.locators.FAQ_QUESTION_SIX)

    def click_faq_question_seven(self):
        self.click(self.locators.FAQ_QUESTION_SEVEN)

    def click_faq_question_eight(self):
        self.click(self.locators.FAQ_QUESTION_EIGHT)

    def text_answer_for_question_one(self):
        return self.get_text(self.locators.FAQ_ANSWER_ONE)

    def text_answer_for_question_two(self):
        return self.get_text(self.locators.FAQ_ANSWER_TWO)

    def text_answer_for_question_three(self):
        return self.get_text(self.locators.FAQ_ANSWER_THREE)

    def text_answer_for_question_four(self):
        return self.get_text(self.locators.FAQ_ANSWER_FOUR)

    def text_answer_for_question_five(self):
        return self.get_text(self.locators.FAQ_ANSWER_FIVE)

    def text_answer_for_question_six(self):
        return self.get_text(self.locators.FAQ_ANSWER_SIX)

    def text_answer_for_question_seven(self):
        return self.get_text(self.locators.FAQ_ANSWER_SEVEN)

    def text_answer_for_question_eight(self):
        return self.get_text(self.locators.FAQ_ANSWER_EIGHT)
