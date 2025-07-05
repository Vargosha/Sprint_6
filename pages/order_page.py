from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderPageMethods:
    def __init__(self,driver):
        self.driver = driver
        self.locators = OrderPageLocators()

    # Шаг 1
    def wait_for_load_order_page_step_one(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.locators.NEXT_BUTTON))

    def click_next_button(self):
        self.driver.find_element(*self.locators.NEXT_BUTTON).click()

    def set_name(self,name):
        self.driver.find_element(*self.locators.NAME_INPUT_FIELD).send_keys(name)

    def set_surname(self,surname):
        self.driver.find_element(*self.locators.SURNAME_INPUT_FIELD).send_keys(surname)

    def set_adress(self,adress):
        self.driver.find_element(*self.locators.ADRESS_INPUT_FIELD).send_keys(adress)

    def set_metro_station(self,station):
        metro_stations = {
            'Бульвар Рокоссовского': self.locators.METRO_STATION_ROKOSSOVSKY_BOULEVARD,
            'Комсомольская': self.locators.METRO_STATION_KOMSOMOLSKAYA
        }
        self.driver.find_element(*self.locators.METRO_STATION_SELECT_FIELD).click()
        self.driver.find_element(*metro_stations[station]).click()

    def set_phone_number(self,phone_number):
        self.driver.find_element(*self.locators.PHONE_NUMBER_INPUT_FIELD).send_keys(phone_number)

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
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.locators.ORDER_BUTTON))

    def click_order_button(self):
        self.driver.find_element(*self.locators.ORDER_BUTTON).click()

    def click_header_disclaimer(self):
        self.driver.find_element(*self.locators.HEADER_DISCLAIMER).click()

    def set_delivery_date(self,delivery_date):
        self.driver.find_element(*self.locators.DELIVERY_DATE_INPUT_FIELD).send_keys(delivery_date)

    def set_rental_period(self,period):
        days_period = {
            'Сутки': self.locators.RENTAL_PERIOD_ONE_DAY_BUTTON,
            'Трое суток':self.locators.RENTAL_PERIOD_THREE_DAYS_BUTTON
        }
        self.driver.find_element(*self.locators.RENTAL_PERIOD_SELECT_FIELD).click()
        self.driver.find_element(*days_period[period]).click()

    def set_step_two(self,delivery_date,period):
        self.wait_for_load_order_page_step_two()
        self.set_delivery_date(delivery_date)
        self.click_header_disclaimer()
        self.set_rental_period(period)
        self.click_order_button()

    # Шаг 3
    def wait_for_load_order_page_step_three(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.locators.CONFIRM_BUTTON))

    def click_confirm_button(self):
        self.driver.find_element(*self.locators.CONFIRM_BUTTON).click()

    def set_step_three(self):
        self.wait_for_load_order_page_step_three()
        self.click_confirm_button()

    # Шаг 4
    def wait_for_load_order_page_step_four(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.locators.SHOW_STATUS_ORDER_BUTTON))

    def click_show_status_order_button(self):
        self.driver.find_element(*self.locators.SHOW_STATUS_ORDER_BUTTON).click()

    def check_show_status_order_button_is_enabled(self):
        return self.driver.find_element(*self.locators.SHOW_STATUS_ORDER_BUTTON).is_enabled()

    def set_step_four(self):
        self.wait_for_load_order_page_step_four()
        self.click_show_status_order_button()
