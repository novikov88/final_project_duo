from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging
import allure


class BasePage:
    def __init__(self, browser, wait=3):
        self.browser = browser
        self.wait = WebDriverWait(browser, wait)
        self.actions = ActionChains(browser)

        self.logger = logging.getLogger(type(self).__name__)
        file_handler = logging.FileHandler(f"logs/{self.browser.test_name}.log")
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.handlers.clear()
        self.logger.addHandler(file_handler)
        self.logger.setLevel(level=self.browser.log_level)

    def add_screenshot_to_allure(self, locator):
        allure.attach(body=self.browser.get_screenshot_as_png(),
                      name=f"{locator}",
                      attachment_type=allure.attachment_type.PNG)

    def _click(self, locator: tuple):
        with allure.step(f"Кликаю в элемент {locator}"):
            try:
                self.logger.info(f"Click on element: {locator}")
                self.wait.until(EC.element_to_be_clickable(locator)).click()
            except TimeoutException:
                self.add_screenshot_to_allure(locator)
                self.logger.info(f"Failed to click on element: {locator} on page {self.browser.current_url}")
                raise AssertionError(f"(!)Failed to click on element: {locator} on page {self.browser.current_url}(!)")

    def _element(self, locator: tuple):
        with allure.step(f"Ищу элемент {locator}"):
            try:
                self.logger.info(f"Check if element {locator} is present")
                return self.wait.until(EC.visibility_of_element_located(locator))
            except TimeoutException:
                self.add_screenshot_to_allure(locator)
                self.logger.info(f"(!)Cant find element by locator: {locator} on page {self.browser.current_url}(!)")
                raise AssertionError(f"Cant find element by locator: {locator} on page {self.browser.current_url}")

    def _elements(self, locator: tuple):
        with allure.step(f"Ищу все элементы {locator}"):
            try:
                self.logger.info(f"Check if elements {locator} is present")
                return self.wait.until(EC.visibility_of_all_elements_located(locator))
            except TimeoutException:
                self.add_screenshot_to_allure(locator)
                self.logger.info(f"(!)Cant find elements by locator: {locator} on page {self.browser.current_url}(!)")
                raise AssertionError(f"Cant find elements by locator: {locator} on page {self.browser.current_url}")

    def _input(self, locator, value):
        with allure.step(f"Ввожу '{value}' в элемент {locator}"):
            try:
                self.logger.info(f"Input: {value} in input: {locator}")
                find_field = self.wait.until(EC.presence_of_element_located(locator))
                find_field.click()
                find_field.clear()
                find_field.send_keys(value)
            except TimeoutException:
                self.add_screenshot_to_allure(locator)
                self.logger.info(f"(!)Failed to complete the field: {locator} on page {self.browser.current_url}(!)")
                raise AssertionError(f"Failed to complete the field: {locator} on page {self.browser.current_url}")

    def _mouse_hover(self, locator: tuple):
        with allure.step(f"Навожу на элемент {locator}"):
            try:
                self.logger.info(f"Hover over an element {locator}")
                ActionChains(self.browser).move_to_element(
                    self.wait.until(EC.visibility_of_element_located(locator))).perform()
            except TimeoutException:
                self.add_screenshot_to_allure(locator)
                self.logger.info(f"(!)Failed to hover over element : {locator} on page {self.browser.current_url}(!)")
                raise AssertionError(f"Failed to hover over element : {locator} on page {self.browser.current_url}")
