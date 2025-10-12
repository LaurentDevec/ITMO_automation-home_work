import pytest
from selenium import webdriver


class test_check_text:
    @pytest.fixture(scope="function")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.main_page = MainPage(self.driver)
        yield
        self.driver.quit()

    def test_footer_text(self, setup):
        """Тест кейс 1: Проверка текста в подвале"""
        # a. Перейти на страницу 'https://demoqa.com/'
        self.driver.get('https://demoqa.com/')

        # b. Проверить что текст в подвале == ‘© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.’
        expected_footer_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
        actual_footer_text = self.main_page.get_footer_text()

        assert actual_footer_text == expected_footer_text, \
            f"Текст в подвале не совпадает. Ожидалось: '{expected_footer_text}', Получено: '{actual_footer_text}'"

    def test_center_text_on_elements_page(self, setup):
        """Тест кейс 2: Проверка текста на странице Elements"""
        # a. Перейти на страницу 'https://demoqa.com/'
        self.driver.get('https://demoqa.com/')

        # b. Через кнопку перейти на страницу 'https://demoqa.com/elements'
        self.main_page.click_elements_button()

        # Проверяем, что перешли на правильную страницу
        assert "elements" in self.driver.current_url.lower(), "Не удалось перейти на страницу Elements"

        # c. Проверить что текст по центру == 'Please select an item from left to start practice.'
        expected_center_text = 'Please select an item from left to start practice.'
        actual_center_text = self.main_page.get_center_text()

        assert actual_center_text == expected_center_text, \
            f"Текст по центру не совпадает. Ожидалось: '{expected_center_text}', Получено: '{actual_center_text}'"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])