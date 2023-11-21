# General imports
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Import options for headless mode
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome",
    )

@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    # Default driver value
    driver = ""

    # Option setup to run in headless mode
    options = Options()
    # options.add_argument('--headless')

    # Setup
    print(f"\nSetting up: {browser} driver")
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    # Implicit wait setup for our framework
    driver.implicitly_wait(10)
    yield driver

    # Tear down
    print(f"\nTear down: {browser} driver")
    driver.quit()