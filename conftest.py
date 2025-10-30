import pytest
from selenium import webdriver

# Меняй здесь браузер
BROWSER = "chrome" # или "firefox"

@pytest.fixture
def driver():
    """Фикстура с выбором браузера через переменную"""
    if BROWSER == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    
    yield driver
    driver.quit()