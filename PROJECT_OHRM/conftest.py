import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Utilities.ReadConfig import get_config


@pytest.fixture(scope="function")
def test_setup_and_down(request):

    browser = get_config("browser and url", "browser").lower()
    url = get_config("browser and url", "url")

    if browser == "chrome":
        options = Options()
       
        #options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    elif browser == "edge":
        options = EdgeOptions()
       
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options
        )

    elif browser == "firefox":
        options = FirefoxOptions()
       
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )

    else:
        raise Exception("Browser Not Supported")

   
    driver.set_window_size(1920, 1080)


  
    driver.get(url)

   
    wait = WebDriverWait(driver, 30)

    request.cls.driver = driver
    request.cls.wait = wait

    yield

    driver.quit()
