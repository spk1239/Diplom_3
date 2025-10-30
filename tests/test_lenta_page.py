from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage
from locators.construct_page_locators import ConstructPageLocators
import pytest


class TestConstructPage():

    def test_lenta_button_click(self, driver):
        
        base_page = BasePage(driver)

        base_page.get_urls(Urls.STELLAR_BURGER_CONSTUCT)

        base_page.click_to_element(BasePageLocators.LENTA_ORDERS)   

        assert base_page.current_url("https://stellarburgers.education-services.ru/feed")


