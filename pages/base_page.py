from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure

class BasePage():

    def __init__(self, driver):

        self.driver = driver

    @allure.step("Скролим до нужного элемента")
    def scroll_to_the_element(self, locator):

        element = self.driver.find_element(*locator)

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Ждем 10 секунд')
    def wait(self):
        WebDriverWait(self.driver, 15)
    
    @allure.step("Ждем появления элемента")
    def wait_element(self, locator):

        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    @allure.step('Ждем URL')
    def wait_url(self, url):

        WebDriverWait(self.driver, 15).until(EC.url_contains(url))

    @allure.step("Жмем на элемент")
    def click_to_element(self, element):
          
        self.driver.find_element(*element).click()

    @allure.step('Ищем элемент')
    def find_element(self, element):

        self.driver.find_element(*element)

    @allure.step('Вводим значение')
    def send_keys(self, locator, element):

        self.driver.find_element(*locator).send_keys(element)

    @allure.step('Проверяем что элемент появился на экране')
    def element_is_displayed(self, locator):

        element = self.driver.find_element(*locator)
        
        return element.is_displayed()

    @allure.step("Смена окна")
    def switch_window(self):

        windows = self.driver.window_handles
        
        self.driver.switch_to.window(windows[-1])

    @allure.step('Проверяем URL')    
    def current_url(self, locator):
        
        return self.driver.current_url == locator