from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
import allure


class HomePageMethods(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.locators = HomePageLocators()

    @allure.step('Ждем открытия главной страницы')
    def wait_for_load_home_page(self):
        return self.is_element_visible(self.locators.COOKIES_ACCEPT_BUTTON)

    @allure.step('Нажимаем на кнопку Принять куки')
    def click_cookies_accept_button(self):
        self.click(self.locators.COOKIES_ACCEPT_BUTTON)

    @allure.step('Нажимаем на Логотип Яндекса')
    def click_yandex_logo_button(self):
        self.click(self.locators.YANDEX_LOGO_BUTTON)

    @allure.step('Нажимаем на Логотип Скутера')
    def click_scooter_logo_button(self):
        self.click(self.locators.SCOOTER_LOGO_BUTTON)

    @allure.step('Нажимаем на Верхнюю кнопку Заказать')
    def click_header_order_button(self):
        self.click(self.locators.HEADER_ORDER_BUTTON)

    @allure.step('Нажимаем на нижнюю кнопку Заказать')
    def click_bottom_order_button(self):
        self.click(self.locators.BOTTOM_ORDER_BUTTON)

    def click_faq_question(self,by_locator):
        element = self.find_element(by_locator)
        question_text = element.text
        with allure.step(f"Нажимаем на FAQ вопрос: '{question_text}'"):
            element.click()

    def text_answer_for_question(self,by_locator):
        answer_text = self.get_text(by_locator)
        with allure.step(f"Получаем текст ответа: '{answer_text}'"):
            return answer_text
