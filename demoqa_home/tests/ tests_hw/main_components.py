from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Main_components:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, value):
        """Найти элемент с ожиданием"""
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def find_elements(self, by, value):
        """Найти несколько элементов с ожиданием"""
        return self.wait.until(EC.presence_of_all_elements_located((by, value)))

    def get_text(self, by, value):
        """Получить текст из элемента"""
        try:
            element = self.find_element(by, value)
            return str(element.text)
        except Exception as e:
            print(f"Ошибка при получении текста: {e}")
            return ""

    def click_element(self, by, value):
        """Кликнуть по элементу"""
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def is_element_visible(self, by, value):
        """Проверить видимость элемента"""
        try:
            element = self.find_element(by, value)
            return element.is_displayed()
        except:
            return False