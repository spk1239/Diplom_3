import pytest
from selenium import webdriver
import requests
from faker import Faker
from urls import Urls 

class WebdriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name == "firefox":
            return webdriver.Firefox()
        elif browser_name == "chrome":
            return webdriver.Chrome()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

# Эта функция добавляет возможность передачи параметра --browser в командной строке pytest
def pytest_addoption(parser):
    parser.addoption(
    "--browser", action="store", default="chrome", help="Выбор браузера: 'chrome' или 'firefox'.")

@pytest.fixture
def driver(request):
    # Получаем параметр браузера из командной строки
    browser_name = request.config.getoption("--browser")
    # Создаем и возвращаем соответствующий драйвер
    driver = WebdriverFactory.get_webdriver(browser_name)
    driver.maximize_window()  # Открытие окна на весь экран
    yield driver
    driver.quit()

@pytest.fixture
def login_user():
    fake = Faker(locale="ru_RU")
    
    payload = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }

    requests.post(f'{Urls.STELLAR_BURGER_CONSTUCT}/api/auth/register', data=payload)
    
    login_response = requests.post(f"{Urls.STELLAR_BURGER_CONSTUCT}/api/auth/login", data={
        "email": payload["email"],
        "password": payload["password"]
    })
    
    access_token = login_response.json()["accessToken"]
    
    # Возвращаем словарь с данными пользователя и токеном
    user_data = {
        "email": payload["email"],
        "password": payload["password"],
        "name": payload["name"],
        "accessToken": access_token
    }
    
    yield user_data
    
    headers = {"Authorization": f"Bearer {access_token}"}
    requests.delete(f"{Urls.STELLAR_BURGER_CONSTUCT}/api/auth/user", headers=headers)