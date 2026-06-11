import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from Utilities.ReadConfig import get_config


@pytest.fixture(scope="function")
def test_setup_and_down(request):

    browser = get_config(
        "browser and url",
        "browser"
    ).lower()

    url = get_config(
        "browser and url",
        "url"
    )

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "edge":
        driver = webdriver.Edge()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    else:
        raise Exception("Browser Not Supported")

    driver.maximize_window()

    driver.get(url)

    wait = WebDriverWait(driver, 20)

    request.cls.driver = driver
    request.cls.wait = wait

    yield

    driver.quit()