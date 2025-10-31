from selenium.webdriver.common.by import By
import allure
from locators.construct_page_locators import ConstructPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage

class Profile(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.title("Логин на главной странице")
    def login_in_main_page(self, email, password):

        self.click_to_element(ConstructPageLocators.BUTTON_IN_ACCOUNT)
        self.send_keys(ProfilePageLocators.EMAIL_INPUT, email)
        self.send_keys(ProfilePageLocators.PASSWORD_INPUT, password)
        self.click_to_element(ProfilePageLocators.BUTTON_LOGIN)
        
        self.wait_element(ConstructPageLocators.BUTTON_ORDER)

    @allure.title("Создание заказа бургера")
    def create_order_burger(self, element):
        self.drag_and_drop(element, ConstructPageLocators.BURGER_ORDER_LIST)
        self.click_to_element(ConstructPageLocators.BUTTON_ORDER)

    @allure.title("Открыть детали ингредиента")
    def open_ingredient_details(self):
        self.click_to_element_js(ConstructPageLocators.BUN_INGRIDIENT)

    @allure.title("Закрыть окно деталей ингредиента")
    def close_ingredient_details(self):
        self.click_to_element_js(ConstructPageLocators.WINDOW_CROSS)

    @allure.title("Получить счетчик ингредиента")
    def get_ingredient_counter(self):
        return self.find_element(ConstructPageLocators.BUN_COUNTER).text

    @allure.title("Ожидание появления номера заказа")
    def wait_for_order_number(self):
        self.wait_element(ConstructPageLocators.NUMBER_ORDER)

    @allure.title("Получить номер заказа")
    def get_order_number(self):
        return self.find_element(ConstructPageLocators.NUMBER_ORDER).text

    @allure.title("Закрыть окно заказа")
    def close_order_window(self):
        self.click_to_element_js(ConstructPageLocators.CLOSE_BUTTON_ORDER_WINDOW)