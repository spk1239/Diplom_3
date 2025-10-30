from data import Data
from pages.base_page import BasePage
import allure
from locators.construct_page_locators import ConstructPageLocators
from locators.profile_page_locators import ProfilePageLocators

class Profile(BasePage):

    def __init__(self, driver):

        super().__init__(driver)

    @allure.title("Вход тестовым пользователем")
    def login_in_main_page(self):

        self.find_element(ConstructPageLocators.BUTTON_IN_ACCOUNT).click()

        self.find_element(ProfilePageLocators.EMAIL_INPUT).send_keys(Data.test_user["email"])

        self.find_element(ProfilePageLocators.PASSWORD_INPUT).send_keys(Data.test_user["password"])

        self.find_element(ProfilePageLocators.BUTTON_LOGIN).click()
