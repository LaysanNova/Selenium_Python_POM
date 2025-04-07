import os
import time

from pages.home_page import HomePage
from pages.dynamic_id_page import DynamicIdPage
from pages.class_attribute_page import ClassAttributePage
from pages.hidden_layers_page import HiddenLayersPage
from pages.load_delay_page import LoadDelayPage

def test_navigate_to_dynamic_id(browser, base_url):
    home = HomePage(browser)
    dynamic = DynamicIdPage(browser)

    home.open(base_url)
    home.go_to_dynamic_id()

    assert dynamic.is_heading_visible()
    assert dynamic.get_heading_text() == "Dynamic ID"

def test_navigate_to_class_attribute(browser, base_url):
    home = HomePage(browser)
    page = ClassAttributePage(browser)

    home.open(base_url)
    home.go_to_class_attribute()

    assert page.is_heading_visible()
    assert page.get_heading_text() == "Class Attribute"

def test_navigate_to_hidden_layers(browser, base_url):
    home = HomePage(browser)
    page = HiddenLayersPage(browser)

    home.open(base_url)
    home.go_to_hidden_layers()

    assert page.is_heading_visible()
    assert page.get_heading_text() == "Hidden Layers"

def test_navigate_to_load_delay(browser, base_url):
    home = HomePage(browser)
    page = LoadDelayPage(browser)

    home.open(base_url)
    home.go_to_load_delay()

    assert page.is_heading_visible()
    assert page.get_heading_text() == "Load Delays"

# def test_load_delay_with_timer(browser, base_url):
#     home = HomePage(browser)
#     page = LoadDelayPage(browser)
#
#     home.open(base_url)
#     home.go_to_load_delay()
#
#     start = time.time()
#     assert page.is_heading_visible()
#     end = time.time()
#
#     duration = round(end - start, 2)
#     print(f"⏱ Время ожидания загрузки: {duration} секунд")
#
#     assert page.get_heading_text() == "Load Delays"
