import os
import json
import pytest
import allure
import logging
import datetime
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=('chrome', 'firefox', 'opera'))
    parser.addoption("--executor", action="store", default="192.168.1.70")
    parser.addoption("--url", default="https://www.duolingo.com")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/Downloads/drivers"))
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--bv")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--videos", action="store_true")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    drivers = request.config.getoption("--drivers")
    log_level = request.config.getoption("--log_level")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    if executor == 'local':
        logger.info(f"Starting local environment: {url}, browser: {browser}")
        if browser == 'chrome':
            options = ChromeOptions()
            if headless:
                options.headless = True
            driver = webdriver.Chrome(executable_path=f'{drivers}/chromedriver', options=options)
        elif browser == 'firefox':
            options = FirefoxOptions()
            if headless:
                options.headless = True
            driver = webdriver.Firefox(executable_path=f'{drivers}/geckodriver', options=options)
        elif browser == 'opera':
            options = Options()
            options.add_experimental_option('w3c', True)
            if headless:
                options.headless = True
            driver = webdriver.Opera(executable_path=f'{drivers}/operadriver', options=options)

        else:
            raise ValueError("Driver is not supported")

    else:
        executor_url = f"http://{executor}:4444/wd/hub"
        logger.info(f"Starting a remote environment: {executor_url}, browser: {browser}")
        caps = {
            "browserName": browser,
            "browserVersion": version,
            "name": "Vladimir",
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs,
                "sessionTimeout": "2m"
            },
            'acceptSslCerts': True,
            'acceptInsecureCerts': True,
            'timeZone': 'Europe/Moscow',
            'goog:chromeOptions': {}
        }

        options = Options()
        if browser == 'opera':
            options.add_experimental_option('w3c', True)
        driver = webdriver.Remote(command_executor=executor_url,
                                  desired_capabilities=caps,
                                  options=options)

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name
    start = datetime.datetime.now()
    logger.info("===> Test {} started at {}".format(request.node.name, datetime.datetime.now()))

    driver.maximize_window()

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities),
        attachment_type=allure.attachment_type.JSON
    )

    def fin():
        driver.quit()
        end = datetime.datetime.now()
        logger.info("===> Test {} finished at {}".format(request.node.name, datetime.datetime.now()))
        logger.info(f"The test time was: {end - start}")

    request.addfinalizer(fin)

    def open_path(path=""):
        return driver.get(url + path)

    driver.maximize_window()
    driver.open = open_path
    driver.open()
    return driver
