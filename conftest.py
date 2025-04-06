import pytest
from selenium import webdriver
from utils.env_loader import load_env
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser name: chrome or firefox"
    )
    parser.addoption(
        "--env", action="store", default="dev", help="Environment name: dev/staging/prod"
    )

@pytest.fixture(scope="session", autouse=True)
def load_environment(request):
    env_name = request.config.getoption("--env")
    load_env(env_name)

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        chrome_options = Options()
        chrome_options.add_argument("--log-level=3")
        driver = webdriver.Chrome(options=chrome_options)

    yield driver
    driver.quit()