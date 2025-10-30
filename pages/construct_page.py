import allure
from locators.construct_page_locators import ConstructPageLocators
from pages.base_page import BasePage


class Construct(BasePage):

    def __init__(self, driver):

        super().__init__(driver)

    @allure.title("Создание заказа")
    def create_order_burger(self,element):

        self.drag_and_drop(element, ConstructPageLocators.BURGER_ORDER_LIST)

        self.click_to_element(ConstructPageLocators.BUTTON_ORDER)