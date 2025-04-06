import pytest
from selenium import webdriver
from utils.env_loader import load_env
import os

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="env name: dev/staging/prod")

@pytest.fixture(scope="session", autouse=True)
def load_environment(request):
    env_name = request.config.getoption("--env")
    load_env(env_name)

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()