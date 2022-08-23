import os
import time
import allure
import random
from faker import Faker
from dotenv import load_dotenv
from page_objects.MainPage import MainPage
from page_objects.LoginPage import LoginPage
from page_objects.WelcomePage import WelcomePage
from page_objects.AccountPage import AccountPage
from page_objects.RegistrationPage import RegistrationPage

# загружаем переменные окружения
load_dotenv()

# объявляем переменные из переменных окружения
LOGIN1 = os.getenv('LOGIN1')
LOGIN2 = os.getenv('LOGIN2')
PASSWORD = os.getenv('PASSWORD')

# создаем экземпляр класса Faker для генерации фейковых данных
fake = Faker()


@allure.feature("Learning languages")
@allure.title("Проверка количества доступных карточек языков")
def test_count_number_of_cards(browser):
    """Шаги:
    1. На главной странице нажать кнопку "GET STARTED"
    2. Проверить количество карточек с языками"""
    MainPage(browser).go_to_training()
    MainPage(browser).count_of_cards()


@allure.feature("Login page")
@allure.title("Проверка элементов на странице логина")
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
    MainPage(browser).go_to_login()
    LoginPage(browser).check_close_button()
    LoginPage(browser).check_sign_up_button()
    LoginPage(browser).check_email_input()
    LoginPage(browser).check_password_input()
    LoginPage(browser).check_forgot_link()
    LoginPage(browser).check_log_in_button()
    LoginPage(browser).check_facebook_button()
    LoginPage(browser).check_google_button()
    LoginPage(browser).check_terms_link()
    LoginPage(browser).check_privacy_policy()


@allure.feature("Registration page")
@allure.title("Проверка элементов на странице регистрации")
def test_check_elements_registration_page(browser):
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
    MainPage(browser).go_to_login()
    LoginPage(browser).go_to_registration()
    RegistrationPage(browser).check_close_button()
    RegistrationPage(browser).check_log_in_button()
    RegistrationPage(browser).check_age_input()
    RegistrationPage(browser).check_name_input()
    RegistrationPage(browser).check_email_input()
    RegistrationPage(browser).check_password_input()
    RegistrationPage(browser).check_create_account_button()
    RegistrationPage(browser).check_facebook_button()
    RegistrationPage(browser).check_google_button()
    RegistrationPage(browser).check_terms_link()
    RegistrationPage(browser).check_privacy_policy()


@allure.feature("Login")
@allure.title("Авторизация с невалидными данными")
def test_invalid_login_fake_data(browser):
    """Шаги:
    1. На главной странице нажать кнопку "I ALREADY HAVE AN ACCOUNT"
    2. Заполнить поле "Email or username" и "Password" несуществующими значениями
    3. Нажать на кнопку "LOG IN"
    4. Проверить наличие предупреждения/ошибки о невалидном логине"""
    MainPage(browser).go_to_login()
    LoginPage(browser).enter_email(fake.email())
    LoginPage(browser).enter_password(fake.password())
    LoginPage(browser).click_login_button()
    LoginPage(browser).check_error_text()


@allure.feature("Login")
@allure.title("Авторизация с незаполненными полями")
def test_invalid_login_empty_fields(browser):
    """Шаги:
    1. На главной странице нажать кнопку "I ALREADY HAVE AN ACCOUNT"
    2. Не заполняя поля "Email or username" и "Password" нажать на кнопку "LOG IN"
    3. Проверить наличие предупреждения/ошибки у полей 'Email or username' и 'Password'"""
    MainPage(browser).go_to_login()
    LoginPage(browser).click_login_button()
    LoginPage(browser).check_error_text_email()
    LoginPage(browser).check_error_text_password()


@allure.feature("Registration")
@allure.title("Успешная регистрация")
def test_successful_registration(browser):
    """Шаги:
    1. На главной странице нажать кнопку "I ALREADY HAVE AN ACCOUNT"
    2. Нажать на кнопку "SIGN UP"
    3. Заполнить поля "Age", "Name (optional)", "Email" и "Password"
    4. Нажать на кнопку "Create account"
    5. Проверить что аккаунт успешно создан и начался урок"""
    MainPage(browser).go_to_login()
    LoginPage(browser).go_to_registration()
    RegistrationPage(browser).enter_age(random.randint(5, 99))
    RegistrationPage(browser).enter_first_name((fake.first_name() + 'c1a1'))
    RegistrationPage(browser).enter_email(fake.email())
    RegistrationPage(browser).enter_password(fake.password())
    RegistrationPage(browser).click_create_account()
    # не успевает получить данные поэтому техническая задержка в 2,5 сек
    time.sleep(2.5)
    WelcomePage(browser).check_title()
    WelcomePage(browser).count_of_cards()


@allure.feature("Login")
@allure.title("Логин нового пользователя")
def test_successful_login_new_account(browser):
    """Шаги:
    1. На главной странице нажать кнопку "I ALREADY HAVE AN ACCOUNT"
    2. Заполнить поля "Email or username" и "Password" валидными значениями
    3. Нажать на кнопку "LOG IN"
    4. Проверить что прошла успешная авторизация"""
    MainPage(browser).go_to_login()
    LoginPage(browser).enter_email(LOGIN1)
    LoginPage(browser).enter_password(PASSWORD)
    LoginPage(browser).click_login_button()
    # технический sleep на получение ответа от сервера
    time.sleep(1)
    WelcomePage(browser).check_title()


@allure.feature("Login")
@allure.title("Логин старого пользователя")
def test_login_and_logout_old_account(browser):
    """Шаги:
    1. На главной странице нажать кнопку "I ALREADY HAVE AN ACCOUNT"
    2. Заполнить поля "Email or username" и "Password" валидными значениями старого аккаунта
    3. Нажать на кнопку "LOG IN"
    4. Проверить что прошла успешная авторизация
    5. Произвести LOGOUT и проверить что пользователь не авторизован"""
    MainPage(browser).go_to_login()
    LoginPage(browser).enter_email(LOGIN2)
    LoginPage(browser).enter_password(PASSWORD)
    LoginPage(browser).click_login_button()
    # технический sleep на получение ответа от сервера
    time.sleep(2)
    AccountPage(browser).hover_user_menu()
    AccountPage(browser).click_logout_from_user_menu()
    MainPage(browser).check_title()


@allure.feature("Learning languages")
@allure.title("Проверка количества доступных карточек языков на главной странице")
def test_check_the_number_of_languages(browser):
    """Шаги:
    1. На главной странице нажать кнопку навести курсор на меню "Site language:"
    2. Проверить количество доступных языков к изучению"""
    MainPage(browser).hover_languages()
    MainPage(browser).count_the_number_of_languages()


@allure.feature("Profile")
@allure.title("Проверка смены имени в профиле")
def test_change_name(browser):
    """Шаги:
    1. На главной странице нажать кнопку "I ALREADY HAVE AN ACCOUNT"
    2. Заполнить поля "Email or username" и "Password" валидными значениями старого аккаунта
    3. Нажать на кнопку "LOG IN"
    4. В меню пользователя выбрать 'Your Profile'
    5. Нажать на кнопку 'Edit Profile'
    6. Изменить имя пользователя на новое
    7. Проверить, что имя пользователя изменено"""
    MainPage(browser).go_to_login()
    LoginPage(browser).enter_email(LOGIN2)
    LoginPage(browser).enter_password(PASSWORD)
    LoginPage(browser).click_login_button()
    # технический sleep на получение ответа от сервера
    time.sleep(2)
    AccountPage(browser).hover_user_menu()
    AccountPage(browser).click_your_profile_from_user_menu()
    # технический sleep на получение ответа от сервера
    time.sleep(2)
    AccountPage(browser).click_edit_profile_button()
    new_name = (fake.first_name() + 'otus')
    AccountPage(browser).input_data_in_field(new_name)
    AccountPage(browser).click_save_changes_button()
    AccountPage(browser).hover_user_menu()
    AccountPage(browser).click_your_profile_from_user_menu()
    AccountPage(browser).check_changed_name(new_name)
