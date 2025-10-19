from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SwagLabs(BasePage):

    def exist_icon(self):
        try:
            self.find_element((By.CSS_SELECTOR, 'div.login_logo'))
        except NoSuchElementException:
            return False
        return True

    def exist_username_field(self):
        try:
            self.find_element((By.CSS_SELECTOR, 'input[data-test="username"]'))
        except NoSuchElementException:
            return False
        return True

    def exist_password_field(self):
        try:
            self.find_element((By.CSS_SELECTOR, 'input[data-test="password"]'))
        except NoSuchElementException:
            return False
        return True