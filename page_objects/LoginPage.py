from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class LoginPage(BasePage):
    CLOSE_BUTTON = (By.CSS_SELECTOR, "[data-test='close-button']")
    SIGN_UP_BUTTON = (By.XPATH, "//span[contains(text(), 'Sign up')]")
    EMAIL_FIELD = (By.CSS_SELECTOR, "[data-test='email-input']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[data-test='password-input']")
    FORGOT_TEXT_LINK = (By.XPATH, "//a[contains(text(),'Forgot?')]")
    LOG_IN_BUTTON = (By.CSS_SELECTOR, "[data-test='register-button']")
    FACEBOOK_BUTTON = (By.XPATH, "//span[contains(text(),'Facebook')]")
    GOOGLE_BUTTON = (By.XPATH, "//span[contains(text(), 'Google')]")
    TERMS_TEXT_LINK = (By.XPATH, "//b[contains(text(),'Terms')]")
    PRIVACY_POLICY_TEXT_LINK = (By.XPATH, "//b[contains(text(),'Privacy Policy')]")
    ERROR_TEXT = (By.CSS_SELECTOR, "[data-test='invalid-form-field']")
    ERROR_TEXT_EMAIL = (By.XPATH, "//div[contains(text(),'Invalid email address')]")
    ERROR_TEXT_PASSWORD = (By.XPATH, "//div[contains(text(),'Password too short')]")

    def check_close_button(self):
        self._element(self.CLOSE_BUTTON)

    def check_sign_up_button(self):
        self._element(self.SIGN_UP_BUTTON)

    def check_email_input(self):
        self._element(self.EMAIL_FIELD)

    def check_password_input(self):
        self._element(self.PASSWORD_FIELD)

    def check_forgot_link(self):
        self._element(self.FORGOT_TEXT_LINK)

    def check_log_in_button(self):
        self._element(self.LOG_IN_BUTTON)

    def check_facebook_button(self):
        self._element(self.FACEBOOK_BUTTON)

    def check_google_button(self):
        google_btn = self._elements(self.GOOGLE_BUTTON)
        assert len(google_btn) == 2

    def check_terms_link(self):
        self._element(self.TERMS_TEXT_LINK)

    def check_privacy_policy(self):
        self._element(self.PRIVACY_POLICY_TEXT_LINK)

    def go_to_registration(self):
        self._click(self.SIGN_UP_BUTTON)

    def click_login_button(self):
        self._click(self.LOG_IN_BUTTON)

    def check_error_text(self):
        self._element(self.ERROR_TEXT)

    def check_error_text_email(self):
        self._element(self.ERROR_TEXT_EMAIL)

    def check_error_text_password(self):
        self._element(self.ERROR_TEXT_PASSWORD)

    def enter_email(self, data):
        self._input(self.EMAIL_FIELD, data)

    def enter_password(self, data):
        self._input(self.PASSWORD_FIELD, data)
