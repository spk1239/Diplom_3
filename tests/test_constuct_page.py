from urls import Urls
from locators.base_page_locators import BasePageLocators
from pages.construct_page import Construct
from pages.base_page import BasePage
from locators.construct_page_locators import ConstructPageLocators
import pytest
import allure


class TestConstructPage():
    @allure.title("Проверка кнопки Конструктор в шапке сайта")
    def test_construct_button_click(self, driver):
    
        base_page = BasePage(driver)

        base_page.get_urls(Urls.STELLAR_BURGER_LENTA)

        base_page.click_to_element_js(BasePageLocators.BUTTON_CONSTRUCT)  # ← JS клик

        assert base_page.element_is_displayed(ConstructPageLocators.TEXT_BURGER_CONSTRUCT)

    @allure.title("Проверка открытия окна ингредиента")
    def test_window_ingridient_in_display(self, driver):
        construct_page = Construct(driver)

        construct_page.get_urls("https://stellarburgers.education-services.ru/")
        construct_page.wait_element(ConstructPageLocators.BUN_INGRIDIENT)

        construct_page.wait_element_clickable(ConstructPageLocators.BUN_INGRIDIENT)
    
        construct_page.click_to_element_js(ConstructPageLocators.BUN_INGRIDIENT)

        construct_page.wait_element(ConstructPageLocators.WINDOW_INGRIDIENT)

        assert construct_page.element_is_displayed(ConstructPageLocators.WINDOW_INGRIDIENT)

    @allure.title("Проверка закрытия окна ингредиента")
    def test_close_window_ingridient_click_the_cross(self, driver):

       construct_page = Construct(driver)

       construct_page.get_urls("https://stellarburgers.education-services.ru/")

       construct_page.wait_element(ConstructPageLocators.BUN_INGRIDIENT)

       construct_page.click_to_element_js(ConstructPageLocators.BUN_INGRIDIENT)  # ← JS клик

       close_button = construct_page.find_element(ConstructPageLocators.WINDOW_CROSS)

       construct_page.click_to_element_js(ConstructPageLocators.WINDOW_CROSS)  # ← JS клик

       construct_page.wait()

       class_name = close_button.get_attribute("class")

       assert "Modal_modal_opened__3ISw4" not in class_name

    @allure.title("Проверка добавления ингредиента в заказ")
    def test_ingredient_added_to_an_order(self, driver):

        construct_page = Construct(driver)

        construct_page.get_urls("https://stellarburgers.education-services.ru/")
   
        counter = construct_page.find_element(ConstructPageLocators.BUN_COUNTER)
   
        construct_page.drag_and_drop(ConstructPageLocators.BUN_INGRIDIENT, ConstructPageLocators.BURGER_ORDER_LIST)

        construct_page.wait()

        assert counter.text == "2"