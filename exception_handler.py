from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_element(driver, locator, timeout=2):
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    except TimeoutException:
        driver.save_screenshot("test.png")
        raise AssertionError(f"Не дождался элемент {locator}")


def wait_elements(driver, locator, timeout=2):
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_all_elements_located(locator))
    except TimeoutException:
        driver.save_screenshot("test.png")
        raise AssertionError(f"Не дождался элемент {locator}")
