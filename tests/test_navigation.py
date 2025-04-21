import os
import time

def test_navigate_to_dynamic_id(home_page):
    dynamic = home_page.go_to_dynamic_id()

    assert dynamic.is_heading_visible()
    assert dynamic.get_heading_text() == "Dynamic ID"

def test_navigate_to_class_attribute(home_page):
    classAttributePage = home_page.go_to_class_attribute()

    assert classAttributePage.is_heading_visible()
    assert classAttributePage.get_heading_text() == "Class Attribute"

def test_navigate_to_hidden_layers(home_page):
    hidden_layersPage = home_page.go_to_hidden_layers()

    assert hidden_layersPage.is_heading_visible()
    assert hidden_layersPage.get_heading_text() == "Hidden Layers"

def test_navigate_to_load_delay(home_page):
    load_delayPage = home_page.go_to_load_delay()

    assert load_delayPage.is_heading_visible()
    assert load_delayPage.get_heading_text() == "Load Delays"


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
