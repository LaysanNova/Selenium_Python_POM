import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.env_loader import load_env
import os

# Add command-line option to specify environment (dev, staging, prod)
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="env name: dev/staging/prod")

# Fixture to load environment variables
@pytest.fixture(scope="session", autouse=True)
def load_environment(request):
    env_name = request.config.getoption("--env")
    load_env(env_name)

# Browser fixture to start and stop the Chrome WebDriver
@pytest.fixture
def browser():
    # Set up Chrome WebDriver using webdriver-manager to handle driver installation
    options = webdriver.ChromeOptions()
    # Add any necessary options for headless mode or other configurations
    options.add_argument("--headless")  # Uncomment if running in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    yield driver  # Return the driver instance to the test
    driver.quit()  # Quit the driver after the test is done