from selenium.webdriver.common.by import By

class ConstructPageLocators():

    TEXT_BURGER_CONSTRUCT = [By.XPATH, ".//h1[text()='Соберите бургер']"]

    BUNS_PAGE = (By.XPATH, ".//span[text()='Булки']/parent::div")

    BUN_INGRIDIENT = [By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]']

    BUN_COUNTER = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']/../div/p[@class='counter_counter__num__3nue1']")

    TOPPINGS_PAGE = (By.XPATH, ".//span[text()='Начинки']/parent::div") 

    TOPPING_INGRIDIENT = (By.XPATH, '//p[text()="Мясо бессмертных моллюсков Protostomia"]')

    BUTTON_IN_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")

    WINDOW_INGRIDIENT = (By.XPATH, ".//h2[text()='Детали ингредиента']")

    WINDOW_CROSS = (By.XPATH, ".//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']/div/button")

    BURGER_ORDER_LIST = (By.XPATH, './/span[text()="Перетяните булочку сюда (верх)"]')

