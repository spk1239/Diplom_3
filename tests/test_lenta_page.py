from urls import Urls
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage
from pages.construct_page import Construct
from pages.profile_page import Profile
from pages.lenta_page import Lenta
from locators.construct_page_locators import ConstructPageLocators
from locators.lenta_page_locators import LentaPageLocators
import pytest
import allure


class TestConstructPage():
    @allure.title("Проверка кнопки Лента заказов в шапке сайта")
    def test_lenta_button_click(self, driver):
        
        base_page = BasePage(driver)

        base_page.get_urls(Urls.STELLAR_BURGER_CONSTUCT)

        base_page.click_to_element(BasePageLocators.LENTA_ORDERS)   

        assert base_page.current_url("https://stellarburgers.education-services.ru/feed")

    @pytest.mark.parametrize("locator", [LentaPageLocators.COUNT_ALL_TIME,LentaPageLocators.COUNT_TO_DAY])
    @allure.title("Увеличение счетчика после создания заказа")
    def test_create_order_increases_counter(self, driver, locator):
        profile_page = Profile(driver)
        construct_page = Construct(driver)
        lenta_page = Lenta(driver)

        lenta_page.get_urls(Urls.STELLAR_BURGER_LENTA)
    
        lenta_page.wait_element(locator)
        count_before = int(lenta_page.find_element(locator).text)
    
        lenta_page.click_to_element(BasePageLocators.BUTTON_CONSTRUCT)
    
        profile_page.login_in_main_page()
        construct_page.create_order_burger(ConstructPageLocators.BUN_INGRIDIENT)
    
        construct_page.wait_element(ConstructPageLocators.NUMBER_ORDER)

        construct_page.click_to_element_js(ConstructPageLocators.CLOSE_BUTTON_ORDER_WINDOW)

        construct_page.wait_element_clickable(BasePageLocators.LENTA_ORDERS)
        construct_page.click_to_element_js(BasePageLocators.LENTA_ORDERS)

        lenta_page.wait_url(Urls.STELLAR_BURGER_LENTA)
        lenta_page.wait()
        lenta_page.wait_element(locator)
    
    
        count_after = int(lenta_page.find_element(locator).text)

        lenta_page.wait()

        assert count_after > count_before

    @allure.title("Проверка добавления номера созданного заказа в список в работе")
    def test_create_order_list_order_add_number_order(self, driver):

        profile_page = Profile(driver)
        construct_page = Construct(driver)
        lenta_page = Lenta(driver)

        lenta_page.get_urls(Urls.STELLAR_BURGER_LENTA)
        lenta_page.wait_element(LentaPageLocators.LIST_ORDER)
        orders_before = [order.text for order in lenta_page.find_elements(LentaPageLocators.LIST_ORDER)]
    
        lenta_page.click_to_element(BasePageLocators.BUTTON_CONSTRUCT)
        profile_page.login_in_main_page()
        construct_page.create_order_burger(ConstructPageLocators.BUN_INGRIDIENT)

        construct_page.wait_element(ConstructPageLocators.NUMBER_ORDER)
    
        initial_number = construct_page.find_element(ConstructPageLocators.NUMBER_ORDER).text
    
        construct_page.wait_text_changed(ConstructPageLocators.NUMBER_ORDER, initial_number)
    
        number_order_modal = construct_page.find_element(ConstructPageLocators.NUMBER_ORDER).text
    
        number_order_normalized = number_order_modal.zfill(7)

        construct_page.click_to_element_js(ConstructPageLocators.CLOSE_BUTTON_ORDER_WINDOW)
        construct_page.wait_element_clickable(BasePageLocators.LENTA_ORDERS)
        construct_page.click_to_element_js(BasePageLocators.LENTA_ORDERS)

        lenta_page.wait_url(Urls.STELLAR_BURGER_LENTA)
        lenta_page.wait_element(LentaPageLocators.LIST_ORDER)
    
        lenta_page.wait()
    
        orders_after = [order.text for order in lenta_page.find_elements(LentaPageLocators.LIST_ORDER)]
    
        assert number_order_normalized in orders_after