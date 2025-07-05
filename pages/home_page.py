from locators.home_page_locators import HomePageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePageMethods:
    home_page_url = 'https://qa-scooter.praktikum-services.ru/'

    def __init__(self,driver):
        self.driver = driver
        self.locators = HomePageLocators()

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.locators.COOKIES_ACCEPT_BUTTON))

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def click_cookies_accept_button(self):
        self.driver.find_element(*self.locators.COOKIES_ACCEPT_BUTTON).click()

    def click_yandex_logo_button(self):
        self.driver.find_element(*self.locators.YANDEX_LOGO_BUTTON).click()

    def click_scooter_logo_button(self):
        self.driver.find_element(*self.locators.SCOOTER_LOGO_BUTTON).click()

    def click_header_order_button(self):
        self.driver.find_element(*self.locators.HEADER_ORDER_BUTTON).click()

    def click_bottom_order_button(self):
        self.driver.find_element(*self.locators.BOTTOM_ORDER_BUTTON).click()

    def click_faq_question_one(self):
        self.driver.find_element(*self.locators.FAQ_QUESTION_ONE).click()

    def click_faq_question_two(self):
        self.driver.find_element(*self.locators.FAQ_QUESTION_TWO).click()

    def click_faq_question_three(self):
        self.driver.find_element(*self.locators.FAQ_QUESTION_THREE).click()

    def click_faq_question_four(self):
        self.driver.find_element(*self.locators.FAQ_QUESTION_FOUR).click()

    def click_faq_question_five(self):
        self.driver.find_element(*self.locators.FAQ_QUESTION_FIVE).click()

    def click_faq_question_six(self):
        self.driver.find_element(*self.locators.FAQ_QUESTION_SIX).click()

    def click_faq_question_seven(self):
        self.driver.find_element(*self.locators.FAQ_QUESTION_SEVEN).click()

    def click_faq_question_eight(self):
        self.driver.find_element(*self.locators.FAQ_QUESTION_EIGHT).click()

    def text_answer_for_question_one(self):
        return self.driver.find_element(*self.locators.FAQ_ANSWER_ONE).text

    def text_answer_for_question_two(self):
        return self.driver.find_element(*self.locators.FAQ_ANSWER_TWO).text

    def text_answer_for_question_three(self):
        return self.driver.find_element(*self.locators.FAQ_ANSWER_THREE).text

    def text_answer_for_question_four(self):
        return self.driver.find_element(*self.locators.FAQ_ANSWER_FOUR).text

    def text_answer_for_question_five(self):
        return self.driver.find_element(*self.locators.FAQ_ANSWER_FIVE).text

    def text_answer_for_question_six(self):
        return self.driver.find_element(*self.locators.FAQ_ANSWER_SIX).text

    def text_answer_for_question_seven(self):
        return self.driver.find_element(*self.locators.FAQ_ANSWER_SEVEN).text

    def text_answer_for_question_eight(self):
        return self.driver.find_element(*self.locators.FAQ_ANSWER_EIGHT).text
