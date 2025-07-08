from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPageMethods(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()

    # Шаг 1
    def wait_for_load_order_page_step_one(self):
        return self.is_element_visible(self.locators.NEXT_BUTTON)

    def click_next_button(self):
        self.click(self.locators.NEXT_BUTTON)

    def set_name(self,name):
        self.send_keys(self.locators.NAME_INPUT_FIELD,name)

    def set_surname(self,surname):
        self.send_keys(self.locators.SURNAME_INPUT_FIELD,surname)

    def set_adress(self,adress):
        self.send_keys(self.locators.ADRESS_INPUT_FIELD,adress)

    def set_metro_station(self,station):
        metro_stations = {
            'Бульвар Рокоссовского': self.locators.METRO_STATION_ROKOSSOVSKY_BOULEVARD,
            'Комсомольская': self.locators.METRO_STATION_KOMSOMOLSKAYA
        }
        self.click(self.locators.METRO_STATION_SELECT_FIELD)
        self.click(metro_stations[station])

    def set_phone_number(self,phone_number):
        self.send_keys(self.locators.PHONE_NUMBER_INPUT_FIELD,phone_number)

    def set_step_one(self, name, surname, adress, station, phone_number):
        self.wait_for_load_order_page_step_one()
        self.set_name(name)
        self.set_surname(surname)
        self.set_adress(adress)
        self.set_metro_station(station)
        self.set_phone_number(phone_number)
        self.click_next_button()

    # Шаг 2
    def wait_for_load_order_page_step_two(self):
        return self.is_element_visible(self.locators.ORDER_BUTTON)

    def click_order_button(self):
        self.click(self.locators.ORDER_BUTTON)

    def click_header_disclaimer(self):
        self.click(self.locators.HEADER_DISCLAIMER)

    def set_delivery_date(self,delivery_date):
        self.send_keys(self.locators.DELIVERY_DATE_INPUT_FIELD,delivery_date)

    def set_rental_period(self,period):
        days_period = {
            'Сутки': self.locators.RENTAL_PERIOD_ONE_DAY_BUTTON,
            'Трое суток':self.locators.RENTAL_PERIOD_THREE_DAYS_BUTTON
        }
        self.click(self.locators.RENTAL_PERIOD_SELECT_FIELD)
        self.click(days_period[period])

    def set_step_two(self,delivery_date,period):
        self.wait_for_load_order_page_step_two()
        self.set_delivery_date(delivery_date)
        self.click_header_disclaimer()
        self.set_rental_period(period)
        self.click_order_button()

    # Шаг 3
    def wait_for_load_order_page_step_three(self):
        return self.is_element_visible(self.locators.CONFIRM_BUTTON)

    def click_confirm_button(self):
        self.click(self.locators.CONFIRM_BUTTON)

    def set_step_three(self):
        self.wait_for_load_order_page_step_three()
        self.click_confirm_button()

    # Шаг 4
    def wait_for_load_order_page_step_four(self):
        return self.is_element_visible(self.locators.SHOW_STATUS_ORDER_BUTTON)

    def click_show_status_order_button(self):
        self.click(self.locators.SHOW_STATUS_ORDER_BUTTON)

    def check_show_status_order_button_is_enabled(self):
        return self.find_element(self.locators.SHOW_STATUS_ORDER_BUTTON).is_enabled()

    def set_step_four(self):
        self.wait_for_load_order_page_step_four()
        self.click_show_status_order_button()
