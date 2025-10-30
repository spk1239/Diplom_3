from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.construct_page_locators import ConstructPageLocators
from pages.base_page import BasePage


class Lenta(BasePage):

    def __init__(self, driver):

        super().__init__(driver)