import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTextBox:

    @pytest.fixture(autouse=True)
    def setup(self):
        """Настройка перед каждым тестом"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    def test_text_box_submission(self):
        """Тест заполнения и отправки текстовых полей"""
        # a. Перейти на страницу
        self.driver.get("https://demoqa.com/text-box")

        # Переменные с текстом для ввода
        full_name = "Иван Иванов"
        current_address = "ул. Пушкина, д. Колотушкина, 123456"

        # b. Записать в поля Full Name, Current Address произвольный текст
        full_name_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "userName"))
        )
        full_name_input.send_keys(full_name)

        current_address_input = self.driver.find_element(By.ID, "currentAddress")
        current_address_input.send_keys(current_address)

        # c. Нажать на кнопку submit
        submit_button = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()

        # d. Проверить, что снизу появились 2 элемента с нашим текстом
        # Ждем появления результата
        self.wait.until(
            EC.presence_of_element_located((By.ID, "output"))
        )

        # Проверяем вывод имени
        name_output = self.driver.find_element(By.ID, "name")
        assert full_name in name_output.text, f"Текст '{full_name}' не найден в выводе имени"

        # Проверяем вывод адреса
        address_output = self.driver.find_element(By.ID, "currentAddress")
        assert current_address in address_output.text, f"Текст '{current_address}' не найден в выводе адреса"

        print(f"✓ Введенное имя: {full_name}")
        print(f"✓ Введенный адрес: {current_address}")
        print("✓ Данные успешно отображены в результате")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])