# Diplom_3

Автотесты для сайта "Stellar Burgers"

**Структура проекта:**
- `pages/` - классы страниц в стиле Page Object
- `locators/` - локаторы элементов  
- `tests/` - тестовые сценарии
- `allure_results/` - отчеты Allure

**Запуск тестов:**
```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск в Chrome
pytest tests/ -v --browser=chrome

# Запуск в Firefox  
pytest tests/ -v --browser=firefox

# С отчетом Allure
pytest tests/ -v --alluredir=allure_results
allure serve allure_results
