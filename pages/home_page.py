from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.dynamic_id = (By.LINK_TEXT, "Dynamic ID")
        self.class_attribute = (By.LINK_TEXT, "Class Attribute")
        self.hidden_layers = (By.LINK_TEXT, "Hidden Layers")
        self.load_delay = (By.LINK_TEXT, "Load Delay")

    def open(self, base_url):
        self.driver.get(base_url)

    def go_to_dynamic_id(self):
        self.click(self.dynamic_id)

    def go_to_class_attribute(self):
        self.click(self.class_attribute)

    def go_to_hidden_layers(self):
        self.click(self.hidden_layers)

    def go_to_load_delay(self):
        self.click(self.load_delay)

    def wait_for_page_to_load(self):
        self.wait_for_page_to_load()





