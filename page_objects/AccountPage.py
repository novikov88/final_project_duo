from selenium.webdriver.common.by import By
from page_objects.BasePage import BasePage


class AccountPage(BasePage):
    USER_ICON = (By.CSS_SELECTOR, ".J0tZA")
    LOGOUT_BUTTON_MENU = (By.XPATH, "//span[contains(text(),'Logout')]")
    YOUR_PROFILE_MENU = (By.XPATH, "//span[contains(text(),'Your Profile')]")
    EDIT_PROFILE_BUTTON = (By.XPATH, "//div[contains(text(),'Edit Profile')]")
    NAME_FIELD = (By.CSS_SELECTOR, "#name")
    SAVE_CHANGES_BUTTON = (By.XPATH, "//span[contains(text(), 'Save changes')]")

    def hover_user_menu(self):
        self._mouse_hover(self.USER_ICON)

    def click_logout_from_user_menu(self):
        self._click(self.LOGOUT_BUTTON_MENU)

    def click_your_profile_from_user_menu(self):
        self._click(self.YOUR_PROFILE_MENU)

    def click_edit_profile_button(self):
        self._click(self.EDIT_PROFILE_BUTTON)

    def input_data_in_field(self, data):
        self._input(self.NAME_FIELD, data)

    def click_save_changes_button(self):
        self._click(self.SAVE_CHANGES_BUTTON)

    def check_changed_name(self, new_name):
        # поиск элемента содержащее новое (измененное на прошлом шаге) имя, поэтому пришлось объявить переменную
        # внутри функции
        new_name_text = (By.XPATH, f"//span[contains(text(),{new_name})]")
        self._element(new_name_text)
