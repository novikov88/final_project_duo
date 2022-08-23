from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class WelcomePage(BasePage):
    TITlE_WELCOME = (By.XPATH, "//h1[contains(text(),'Welcome to Duolingo!')]")
    LANGUAGE_CARD = (By.CSS_SELECTOR, "[data-test*='language-card']")

    def check_title(self):
        self._element(self.TITlE_WELCOME)

    def count_of_cards(self):
        count_of_cards = self._elements(self.LANGUAGE_CARD)
        assert len(count_of_cards) == 38
