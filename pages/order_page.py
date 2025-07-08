from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
import allure


class OrderPageMethods(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    # Шаг 1
    @allure.step('Ждем открытия страницы. Шаг 1')
    def wait_for_load_order_page_step_one(self):
        return self.is_element_visible(self.locators.NEXT_BUTTON)

    @allure.step('Нажимаем кнопку Далее')
    def click_next_button(self):
        self.click(self.locators.NEXT_BUTTON)

    @allure.step('Заполняем поле Имя')
    def set_name(self,name):
        self.send_keys(self.locators.NAME_INPUT_FIELD,name)

    @allure.step('Заполняем поле Фамилия')
    def set_surname(self,surname):
        self.send_keys(self.locators.SURNAME_INPUT_FIELD,surname)

    @allure.step('Заполняем поле Адрес')
    def set_adress(self,adress):
        self.send_keys(self.locators.ADRESS_INPUT_FIELD,adress)

    @allure.step('Заполняем поле Станция метро')
    def set_metro_station(self,station):
        metro_stations = {
            'Бульвар Рокоссовского': self.locators.METRO_STATION_ROKOSSOVSKY_BOULEVARD,
            'Комсомольская': self.locators.METRO_STATION_KOMSOMOLSKAYA
        }
        self.click(self.locators.METRO_STATION_SELECT_FIELD)
        self.click(metro_stations[station])

    @allure.step('Заполняем поле Номер телефона')
    def set_phone_number(self,phone_number):
        self.send_keys(self.locators.PHONE_NUMBER_INPUT_FIELD,phone_number)

    @allure.step('Заполняем данные Шаг 1')
    def set_step_one(self, name, surname, adress, station, phone_number):
        self.wait_for_load_order_page_step_one()
        self.set_name(name)
        self.set_surname(surname)
        self.set_adress(adress)
        self.set_metro_station(station)
        self.set_phone_number(phone_number)
        self.click_next_button()

    # Шаг 2
    @allure.step('Ждем открытия страницы. Шаг 2')
    def wait_for_load_order_page_step_two(self):
        return self.is_element_visible(self.locators.ORDER_BUTTON)

    @allure.step('Нажимаем кнопку Заказать')
    def click_order_button(self):
        self.click(self.locators.ORDER_BUTTON)

    @allure.step('Нажимем на дисклеймер Учебный Тренажер, чтобы убрать фокус с поля')
    def click_header_disclaimer(self):
        self.click(self.locators.HEADER_DISCLAIMER)

    @allure.step('Заполняем поле Дата доставки')
    def set_delivery_date(self,delivery_date):
        self.send_keys(self.locators.DELIVERY_DATE_INPUT_FIELD,delivery_date)

    @allure.step('Заполняем поле Срок аренды')
    def set_rental_period(self,period):
        days_period = {
            'Сутки': self.locators.RENTAL_PERIOD_ONE_DAY_BUTTON,
            'Трое суток':self.locators.RENTAL_PERIOD_THREE_DAYS_BUTTON
        }
        self.click(self.locators.RENTAL_PERIOD_SELECT_FIELD)
        self.click(days_period[period])

    @allure.step('Заполняем данные Шаг 2')
    def set_step_two(self,delivery_date,period):
        self.wait_for_load_order_page_step_two()
        self.set_delivery_date(delivery_date)
        self.click_header_disclaimer()
        self.set_rental_period(period)
        self.click_order_button()

    # Шаг 3
    @allure.step('Ждем открытия страницы. Шаг 3')
    def wait_for_load_order_page_step_three(self):
        return self.is_element_visible(self.locators.CONFIRM_BUTTON)

    @allure.step('Нажимаем кнопку Да')
    def click_confirm_button(self):
        self.click(self.locators.CONFIRM_BUTTON)

    @allure.step('Подтверждаем заказ. Шаг 3')
    def set_step_three(self):
        self.wait_for_load_order_page_step_three()
        self.click_confirm_button()

    # Шаг 4
    @allure.step('Ждем открытия страницы Заказа. Шаг 4')
    def wait_for_load_order_page_step_four(self):
        return self.is_element_visible(self.locators.SHOW_STATUS_ORDER_BUTTON)

    @allure.step('Нажимаем кнопку Посмотреть статус')
    def click_show_status_order_button(self):
        self.click(self.locators.SHOW_STATUS_ORDER_BUTTON)

    @allure.step('Проверяем показ кнопки Посмотреть статус')
    def check_show_status_order_button_is_enabled(self):
        return self.find_element(self.locators.SHOW_STATUS_ORDER_BUTTON).is_enabled()

    @allure.step('Завершаем оформление заказа. Шаг 4')
    def set_step_four(self):
        self.wait_for_load_order_page_step_four()
        self.click_show_status_order_button()
