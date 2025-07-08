import pytest
from pages.order_page import OrderPageMethods
from pages.dzen_page import DzenPageMethods
from tests.data import DataForTests
from tests.urls import *
import allure


class TestOrderPage:
    @allure.title('Проверка появления всплывающего окна с сообщением об успешном создании заказа через Верхнюю кнопку Заказать')
    @pytest.mark.parametrize('order_data', DataForTests.ORDER_DATA)
    def test_create_order_via_header_button_with_multiple_data(self,homepage,order_data):
        orderpage = OrderPageMethods(homepage.driver)

        homepage.click_header_order_button()
        orderpage.set_step_one(
            order_data['name'],
            order_data['surname'],
            order_data['address'],
            order_data['station'],
            order_data['phone']
        )
        orderpage.set_step_two(
            order_data['date'],
            order_data['period']
        )
        orderpage.set_step_three()

        assert orderpage.check_show_status_order_button_is_enabled()

    @allure.title('Проверка редиректа на главную страницу Самоката при нажатии на логотип Самоката')
    @pytest.mark.parametrize('order_data', DataForTests.ORDER_DATA)
    def test_scooter_logo_opens_home_page_with_multiple_data(self,homepage,order_data):
        orderpage = OrderPageMethods(homepage.driver)

        homepage.click_header_order_button()
        orderpage.set_step_one(
            order_data['name'],
            order_data['surname'],
            order_data['address'],
            order_data['station'],
            order_data['phone']
        )
        orderpage.set_step_two(
            order_data['date'],
            order_data['period']
        )
        orderpage.set_step_three()
        orderpage.set_step_four()
        homepage.click_scooter_logo_button()

        assert homepage.get_current_url() == HOME_PAGE_URL

    @allure.title('Проверка редиректа в новую вкладку на главную страницу Дзена при нажатии на логотип Яндекса')
    @pytest.mark.parametrize('order_data', DataForTests.ORDER_DATA)
    def test_yandex_logo_opens_dzen_in_new_tab_with_multiple_data(self,homepage,order_data):
        orderpage = OrderPageMethods(homepage.driver)
        dzenpage = DzenPageMethods(homepage.driver)

        homepage.click_header_order_button()
        orderpage.set_step_one(
            order_data['name'],
            order_data['surname'],
            order_data['address'],
            order_data['station'],
            order_data['phone']
        )
        orderpage.set_step_two(
            order_data['date'],
            order_data['period']
        )
        orderpage.set_step_three()
        orderpage.set_step_four()
        homepage.click_yandex_logo_button()

        homepage.switch_to_new_tab()
        dzenpage.wait_for_dzen_tab_opens()

        assert homepage.get_current_url() == DZEN_PAGE_URL

    @allure.title('Проверка появления всплывающего окна с сообщением об успешном создании заказа через Нижнюю кнопку Заказать')
    @pytest.mark.parametrize('order_data', DataForTests.ORDER_DATA)
    def test_create_order_via_footer_button_with_multiple_data(self,homepage,order_data):
        orderpage = OrderPageMethods(homepage.driver)

        homepage.click_bottom_order_button()
        orderpage.set_step_one(
            order_data['name'],
            order_data['surname'],
            order_data['address'],
            order_data['station'],
            order_data['phone']
        )
        orderpage.set_step_two(
            order_data['date'],
            order_data['period']
        )
        orderpage.set_step_three()

        assert orderpage.check_show_status_order_button_is_enabled()
