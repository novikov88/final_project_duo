from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from exception_handler import *
from faker import Faker
import random
import time
import os
from dotenv import load_dotenv

# загружаем переменные окружения
load_dotenv()

# объявляем переменные из переменных окружения
LOGIN1 = os.getenv('LOGIN1')
LOGIN2 = os.getenv('LOGIN2')
PASSWORD = os.getenv('PASSWORD')

# создаем экземпляр класса Faker для генерации данных
fake = Faker()


def test_count_number_of_cards(browser):
    """Шаги:
    1. На главной странице нажать кнопку "GET STARTED"
    2. Проверить количество карточек с языками"""
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='get-started-top']")).click()
    count_of_cards = wait_elements(browser, (By.XPATH, "//h1[contains(text(),'I want to learn...')]/../ul/button"))
    assert len(count_of_cards) == 39


def test_check_elements_login_page(browser):
    """Шаги:
    1. На главной странице нажать кнопку "I ALREADY HAVE AN ACCOUNT"
    2. Проверить наличие элементов на странице:
    - иконка закрытия
    - кнопка "Sign up"
    - поле "Email or username"
    - поле "Password"
    - кнопка "LOG IN"
    - кнопка "Facebook"
    - кнопка "Google"
    - текст-ссылку "Terms"
    - текст ссылку 'Privacy Policy'"""
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='have-account']")).click()
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='close-button']"))
    wait_element(browser, (By.XPATH, "//span[contains(text(), 'Sign up')]"))
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='email-input']"))
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='password-input']"))
    wait_element(browser, (By.XPATH, "//a[contains(text(),'Forgot?')]"))
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='register-button']"))
    wait_element(browser, (By.XPATH, "//span[contains(text(),'Facebook')]"))
    google_btn = wait_elements(browser, (By.XPATH, "//span[contains(text(), 'Google')]"))
    assert len(google_btn) == 2
    wait_element(browser, (By.XPATH, "//b[contains(text(),'Terms')]"))
    wait_element(browser, (By.XPATH, "//b[contains(text(),'Privacy Policy')]"))


def test_check_elements_sign_up_page(browser):
    """Шаги:
        1. На главной странице нажать кнопку "I ALREADY HAVE AN ACCOUNT"
        2. Нажать на кнопку "Sign up"
        2. Проверить наличие элементов на странице:
        - иконка закрытия
        - кнопка "LOGIN"
        - поле "Age"
        - поле "Name (optional)"
        - поле "Email"
        - поле "Password"
        - кнопка "Create account"
        - кнопка "Facebook"
        - кнопка "Google"
        - текст-ссылку "Terms"
        - текст ссылку 'Privacy Policy'"""
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='have-account']")).click()
    wait_element(browser, (By.XPATH, "//span[contains(text(), 'Sign up')]")).click()
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='close-button']"))
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='sign-up-button']"))
    wait_element(browser, (By.CSS_SELECTOR, "[placeholder='Age']"))
    wait_element(browser, (By.CSS_SELECTOR, "[placeholder='Name (optional)']"))
    wait_element(browser, (By.CSS_SELECTOR, "[placeholder='Email']"))
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='register-button']"))
    wait_element(browser, (By.CSS_SELECTOR, "[placeholder='Password']"))
    wait_element(browser, (By.XPATH, "//span[contains(text(),'Facebook')]"))
    google_btn = wait_elements(browser, (By.XPATH, "//span[contains(text(), 'Google')]"))
    assert len(google_btn) == 2
    wait_element(browser, (By.XPATH, "//b[contains(text(),'Terms')]"))
    wait_element(browser, (By.XPATH, "//b[contains(text(),'Privacy Policy')]"))


def test_invalid_login_fake_data(browser):
    """Шаги:
    1. На главной странице нажать кнопку "I ALREADY HAVE AN ACCOUNT"
    2. Заполнить поле "Email or username" и "Password" несуществующими значениями
    3. Нажать на кнопку "LOG IN"
    4. Проверить наличие предупреждения/ошибки о невалидном логине"""
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='have-account']")).click()
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='email-input']")).send_keys(fake.email())
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='password-input']")).send_keys(fake.password())
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='register-button']")).click()
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='invalid-form-field']"))


def test_invalid_login_empty_fields(browser):
    """Шаги:
    1. На главной странице нажать кнопку "I ALREADY HAVE AN ACCOUNT"
    2. Не заполняя поля "Email or username" и "Password" нажать на кнопку "LOG IN"
    3. Проверить наличие предупреждения/ошибки у полей 'Email or username' и 'Password'"""
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='have-account']")).click()
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='register-button']")).click()
    wait_element(browser, (By.XPATH, "//div[contains(text(),'Invalid email address')]"))
    wait_element(browser, (By.XPATH, "//div[contains(text(),'Password too short')]"))


def test_successful_registration(browser):
    """Шаги:
    1. На главной странице нажать кнопку "I ALREADY HAVE AN ACCOUNT"
    2. Нажать на кнопку "SIGN UP"
    3. Заполнить поля "Age", "Name (optional)", "Email" и "Password"
    4. Нажать на кнопку "Create account"
    5. Проверить что аккаунт успешно создан и начался урок"""
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='have-account']")).click()
    wait_element(browser, (By.XPATH, "//span[contains(text(), 'Sign up')]")).click()
    wait_element(browser, (By.CSS_SELECTOR, "[placeholder='Age']")).send_keys(random.randint(5, 99))
    wait_element(browser, (By.CSS_SELECTOR, "[placeholder='Name (optional)']")).send_keys(fake.first_name() + 'cba1')
    wait_element(browser, (By.CSS_SELECTOR, "[placeholder='Email']")).send_keys(fake.email())
    wait_element(browser, (By.CSS_SELECTOR, "[placeholder='Password']")).send_keys(fake.password())
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='register-button']")).click()
    # не успевает получить данные поэтому техническая задержка в 2,5 сек
    time.sleep(2.5)
    wait_element(browser, (By.XPATH, "//h1[contains(text(),'Welcome to Duolingo!')]"))
    count_of_cards = wait_elements(browser, (By.CSS_SELECTOR, "[data-test*='language-card']"))
    assert len(count_of_cards) == 38


def test_successful_login_new_account(browser):
    """Шаги:
    1. На главной странице нажать кнопку "I ALREADY HAVE AN ACCOUNT"
    2. Заполнить поля "Email or username" и "Password" валидными значениями
    3. Нажать на кнопку "LOG IN"
    4. Проверить что прошла успешная авторизация"""
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='have-account']")).click()
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='email-input']")).send_keys(LOGIN1)
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='password-input']")).send_keys(PASSWORD)
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='register-button']")).click()
    time.sleep(1)
    wait_element(browser, (By.XPATH, "//h1[contains(text(),'Welcome to Duolingo!')]"))


def test_login_and_logout_old_account(browser):
    """Шаги:
    1. На главной странице нажать кнопку "I ALREADY HAVE AN ACCOUNT"
    2. Заполнить поля "Email or username" и "Password" валидными значениями старого аккаунта
    3. Нажать на кнопку "LOG IN"
    4. Проверить что прошла успешная авторизация
    5. Произвести LOGOUT и проверить что пользователь не авторизован"""
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='have-account']")).click()
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='email-input']")).send_keys(LOGIN2)
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='password-input']")).send_keys(PASSWORD)
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='register-button']")).click()
    time.sleep(2)
    ActionChains(browser).move_to_element(wait_element(browser, (By.CSS_SELECTOR, ".J0tZA"))).perform()
    wait_element(browser, (By.XPATH, "//span[contains(text(),'Logout')]")).click()
    wait_element(browser, (By.XPATH, "//h1[contains(text(),'The free, fun')]"))


def test_check_the_number_of_languages(browser):
    """Шаги:
    1. На главной странице нажать кнопку навести курсор на меню "Site language:"
    2. Проверить количество доступных языков к изучению"""
    ActionChains(browser).move_to_element(wait_element(browser, (By.XPATH, "//span[contains(text(),'English')]"))).perform()
    number_of_languages = wait_elements(browser, (By.CSS_SELECTOR, "._2bJUZ > li"))
    assert len(number_of_languages) == 25


def test_change_name(browser):
    """Шаги:
    1. На главной странице нажать кнопку "I ALREADY HAVE AN ACCOUNT"
    2. Заполнить поля "Email or username" и "Password" валидными значениями старого аккаунта
    3. Нажать на кнопку "LOG IN"
    4. В меню пользователя выбрать 'Your Profile'
    5. Нажать на кнопку 'Edit Profile'
    6. Изменить имя пользователя на новое
    7. Проверить, что имя пользователя изменено"""
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='have-account']")).click()
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='email-input']")).send_keys(LOGIN2)
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='password-input']")).send_keys(PASSWORD)
    wait_element(browser, (By.CSS_SELECTOR, "[data-test='register-button']")).click()
    time.sleep(2)
    ActionChains(browser).move_to_element(wait_element(browser, (By.CSS_SELECTOR, ".J0tZA"))).perform()
    wait_element(browser, (By.XPATH, "//span[contains(text(),'Your Profile')]")).click()
    time.sleep(2)
    wait_element(browser, (By.XPATH, "//div[contains(text(),'Edit Profile')]")).click()
    name_field = wait_element(browser, (By.CSS_SELECTOR, "#name"))
    name_field.click()
    name_field.clear()
    new_name = (fake.first_name() + 'bbx')
    name_field.send_keys(new_name)
    wait_element(browser, (By.XPATH, "//span[contains(text(), 'Save changes')]")).click()
    ActionChains(browser).move_to_element(wait_element(browser, (By.CSS_SELECTOR, ".J0tZA"))).perform()
    wait_element(browser, (By.XPATH, "//span[contains(text(),'Your Profile')]")).click()
    wait_element(browser, (By.XPATH, f"//span[contains(text(),{new_name})]")).click()
