from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoadDelayPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.heading = (By.TAG_NAME, "h3")

    def is_heading_visible(self):
        return self.is_visible(self.heading)

    def get_heading_text(self):
        return self.get_text(self.heading)