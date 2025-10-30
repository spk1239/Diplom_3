from urls import Urls
from locators.base_page_locators import BasePageLocators
from pages.construct_page import Construct
from pages.base_page import BasePage
from locators.construct_page_locators import ConstructPageLocators
import pytest


class TestConstructPage():

    def test_construct_button_click(self, driver):
        
        base_page = BasePage(driver)

        base_page.get_urls(Urls.STELLAR_BURGER_LENTA)

        base_page.click_to_element(BasePageLocators.BUTTON_CONSTRUCT)

        assert base_page.element_is_displayed(ConstructPageLocators.TEXT_BURGER_CONSTRUCT)

    def test_window_ingridient_in_display(self, driver):

        construct_page = Construct(driver)

        construct_page.get_urls("https://stellarburgers.education-services.ru/")

        construct_page.wait_element(ConstructPageLocators.BUN_INGRIDIENT)

        construct_page.click_to_element(ConstructPageLocators.BUN_INGRIDIENT)

        assert construct_page.element_is_displayed(ConstructPageLocators.WINDOW_INGRIDIENT)

    def test_close_window_ingridient_click_the_cross(self, driver):

        construct_page = Construct(driver)

        construct_page.get_urls("https://stellarburgers.education-services.ru/")

        construct_page.wait_element(ConstructPageLocators.BUN_INGRIDIENT)

        construct_page.click_to_element(ConstructPageLocators.BUN_INGRIDIENT)

        close_button = construct_page.find_element(ConstructPageLocators.WINDOW_CROSS)

        construct_page.click_to_element(ConstructPageLocators.WINDOW_CROSS)

        construct_page.wait()

        class_name = close_button.get_attribute("class")

        assert "Modal_modal_opened__3ISw4" not in class_name

    def test_ingredient_added_to_an_order(self, driver):
        
        construct_page = Construct(driver)

        construct_page.get_urls("https://stellarburgers.education-services.ru/")
   
        counter = construct_page.find_element(ConstructPageLocators.BUN_COUNTER)
   
        construct_page.drag_and_drop(ConstructPageLocators.BUN_INGRIDIENT, ConstructPageLocators.BURGER_ORDER_LIST)

        construct_page.wait()

        assert counter.text == "2"