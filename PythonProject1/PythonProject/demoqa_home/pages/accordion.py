from selenium.webdriver.common.by import By
from pages.base_page import BasePage  # предполагаем, что есть базовый класс

class Accordion(BasePage):
    url = "https://demoqa.com/accordian"

    # Локаторы элементов
    section1_heading = (By.ID, "section1Heading")
    section1_content = (By.CSS_SELECTOR, "#section1Content > p")

    section2_content_1 = (By.CSS_SELECTOR, "#section2Content > p:nth-child(1)")
    section2_content_2 = (By.CSS_SELECTOR, "#section2Content > p:nth-child(2)")
    section3_content = (By.CSS_SELECTOR, "#section3Content > p")

    # Методы для взаимодействия
    def open(self):
        self.browser.get(self.URL)

    def click_section1(self):
        self.browser.find_element(*self.SECTION1_HEADING).click()

    def is_section1_content_visible(self):
        return self.browser.find_element(*self.SECTION1_CONTENT).is_displayed()

    def is_section2_content1_visible(self):
        return self.browser.find_element(*self.SECTION2_CONTENT_1).is_displayed()

    def is_section2_content2_visible(self):
        return self.browser.find_element(*self.SECTION2_CONTENT_2).is_displayed()

    def is_section3_content_visible(self):

        return self.browser.find_element(*self.SECTION3_CONTENT).is_displayed()
