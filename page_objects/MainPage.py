from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class MainPage(BasePage):
    GET_STARTED_BUTTON = (By.CSS_SELECTOR, "[data-test='get-started-top']")
    CARDS_OF_LANGUAGES = (By.XPATH, "//h1[contains(text(),'I want to learn...')]/../ul/button")
    I_ALREADY_HAVE_AN_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[data-test='have-account']")
    TITLE_TEXT = (By.XPATH, "//h1[contains(text(),'The free, fun')]")
    LANGUAGES_DROPDOWN = (By.XPATH, "//span[contains(text(),'English')]")
    LANGUAGES = (By.CSS_SELECTOR, "._2bJUZ > li")

    def go_to_training(self):
        self._click(self.GET_STARTED_BUTTON)

    def count_of_cards(self):
        count_of_cards = self._elements(self.CARDS_OF_LANGUAGES)
        assert len(count_of_cards) == 39

    def go_to_login(self):
        self._click(self.I_ALREADY_HAVE_AN_ACCOUNT_BUTTON)

    def check_title(self):
        self._element(self.TITLE_TEXT)

    def hover_languages(self):
        self._mouse_hover(self.LANGUAGES_DROPDOWN)

    def count_the_number_of_languages(self):
        number_of_languages = self._elements(self.LANGUAGES)
        assert len(number_of_languages) == 25
