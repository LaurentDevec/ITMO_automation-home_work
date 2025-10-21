import base.py
from selenium.webdriver.common.by import By


class Test_check_text:

    def test_footer_text(self, driver):
        """
        Test Case 1: Проверка текста в подвале на главной странице
        """
        # a. перейти на страницу 'https://demoqa.com/'
        driver.get('https://demoqa.com/')

        # b. проверить что текст в подвале == ‘© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.’
        footer_locator = (By.XPATH, "//footer//span")

        # Используем метод get_text для получения текста
        from base_page import Base
        page = Base(driver)
        actual_text = page.get_text(*footer_locator)

        expected_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
        assert actual_text == expected_text, f"Ожидался текст: '{expected_text}', но получен: '{actual_text}'"

    def test_center_text_on_elements_page(self, driver):
        """
        Test Case 2: Проверка текста по центру на странице Elements
        """
        # a. перейти на страницу 'https://demoqa.com/'
        driver.get('https://demoqa.com/')

        # b. через кнопку перейти на страницу 'https://demoqa.com/elements'
        elements_button_locator = (By.XPATH, "//div[@class='card-body']//h5[text()='Elements']")
        driver.find_element(*elements_button_locator).click()

        # Проверяем что перешли на правильную страницу
        assert "elements" in driver.current_url.lower()

        # c. проверить что текст по центру == 'Please select an item from left to start practice.'
        center_text_locator = (By.XPATH,
                               "//div[contains(@class, 'col-md-6') and contains(text(), 'Please select an item')]")

        # Используем метод get_text для получения текста
        from base_page import Base
        page = Base(driver)
        actual_text = page.get_text(*center_text_locator)

        expected_text = 'Please select an item from left to start practice.'
        assert actual_text == expected_text, f"Ожидался текст: '{expected_text}