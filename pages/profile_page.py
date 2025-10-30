from data import Data
from pages.base_page import BasePage
import allure
import requests
from faker import Faker
from locators.construct_page_locators import ConstructPageLocators
from locators.profile_page_locators import ProfilePageLocators

class Profile(BasePage):

    def __init__(self, driver):

        super().__init__(driver)

    @allure.title("Вход пользователем")
    def login_in_main_page(self, email=None, password=None):
    # Используем тестовые данные по умолчанию, если не переданы
        user_email = email or Data.test_user["email"]
        user_password = password or Data.test_user["password"]

        self.find_element(ConstructPageLocators.BUTTON_IN_ACCOUNT).click()
        self.find_element(ProfilePageLocators.EMAIL_INPUT).send_keys(user_email)
        self.find_element(ProfilePageLocators.PASSWORD_INPUT).send_keys(user_password)
        self.find_element(ProfilePageLocators.BUTTON_LOGIN).click()
