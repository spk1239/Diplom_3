from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
import allure

class Construct(BasePage):

    def __init__(self, driver):

        super().__init__(driver)


   