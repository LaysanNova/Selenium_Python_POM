import os

import pytest
from selenium import webdriver

from pages.home_page import HomePage
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

@pytest.fixture(scope="session")
def base_url():
    base_url = os.getenv("BASE_URL")
    if not base_url:
        raise ValueError("BASE_URL is not set")

    return base_url

@pytest.fixture
def home_page(browser, base_url):
    page = HomePage(browser)
    page.open(base_url)  # теперь метод open из BasePage
    return page

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        chrome_options = Options()
        chrome_options.add_argument("--log-level=3")
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=chrome_options)

    yield driver
    driver.quit()