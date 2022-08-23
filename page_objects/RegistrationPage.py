from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class RegistrationPage(BasePage):
    CLOSE_BUTTON = (By.CSS_SELECTOR, "[data-test='close-button']")
    LOG_IN_BUTTON = (By.CSS_SELECTOR, "[data-test='sign-up-button']")
    AGE_FIELD = (By.CSS_SELECTOR, "[placeholder='Age']")
    NAME_FIELD = (By.CSS_SELECTOR, "[placeholder='Name (optional)']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "[data-test='email-input']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[data-test='password-input']")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[data-test='register-button']")
    FACEBOOK_BUTTON = (By.XPATH, "//span[contains(text(),'Facebook')]")
    GOOGLE_BUTTON = (By.XPATH, "//span[contains(text(),'Facebook')]/../../button[2]")
    TERMS_TEXT_LINK = (By.XPATH, "//b[contains(text(),'Terms')]")
    PRIVACY_POLICY_TEXT_LINK = (By.XPATH, "//b[contains(text(),'Privacy Policy')]")

    def check_close_button(self):
        self._element(self.CLOSE_BUTTON)

    def check_log_in_button(self):
        self._element(self.LOG_IN_BUTTON)

    def check_age_input(self):
        self._element(self.AGE_FIELD)

    def check_name_input(self):
        self._element(self.NAME_FIELD)

    def check_email_input(self):
        self._element(self.EMAIL_FIELD)

    def check_password_input(self):
        self._element(self.PASSWORD_FIELD)

    def check_create_account_button(self):
        self._element(self.LOG_IN_BUTTON)

    def check_facebook_button(self):
        self._element(self.FACEBOOK_BUTTON)

    def check_google_button(self):
        google_btn = self._elements(self.GOOGLE_BUTTON)
        assert len(google_btn) == 1

    def check_terms_link(self):
        self._element(self.TERMS_TEXT_LINK)

    def check_privacy_policy(self):
        self._element(self.PRIVACY_POLICY_TEXT_LINK)

    def enter_age(self, data):
        self._input(self.AGE_FIELD, data)

    def enter_first_name(self, data):
        self._input(self.NAME_FIELD, data)

    def enter_email(self, data):
        self._input(self.EMAIL_FIELD, data)

    def enter_password(self, data):
        self._input(self.PASSWORD_FIELD, data)

    def click_create_account(self):
        self._click(self.CREATE_ACCOUNT_BUTTON)
