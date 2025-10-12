import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class TestLoginForm:

    @pytest.fixture(autouse=True)
    def setup(self):
        """Настройка перед каждым тестом"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)
        yield
        self.driver.quit()

    def test_basic_form_fill(self):
        """Базовое заполнение формы"""
        self.driver.get("https://demoqa.com/automation-practice-form")

        # Заполняем основные поля
        self.driver.find_element(By.ID, "firstName").send_keys("Иван")
        self.driver.find_element(By.ID, "lastName").send_keys("Иванов")
        self.driver.find_element(By.ID, "userEmail").send_keys("ivan@example.com")
        self.driver.find_element(By.XPATH, "//label[contains(text(),'Male')]").click()
        self.driver.find_element(By.ID, "userNumber").send_keys("1234567890")

        print("✓ Основные поля формы заполнены")

    def test_state_city_selection(self):
        """Тест заполнения полей State and City"""
        # a. Создайте новый тест кейс
        # b. Реализуйте заполнение поля State and City

        # Переходим на страницу
        self.driver.get("https://demoqa.com/automation-practice-form")

        # Заполняем обязательные поля для активации формы
        self.driver.find_element(By.ID, "firstName").send_keys("Анна")
        self.driver.find_element(By.ID, "lastName").send_keys("Петрова")
        self.driver.find_element(By.XPATH, "//label[contains(text(),'Female')]").click()
        self.driver.find_element(By.ID, "userNumber").send_keys("1234567890")

        # Прокручиваем до полей State and City
        state_section = self.driver.find_element(By.XPATH, "//div[contains(text(),'State and City')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", state_section)

        # Заполняем поле State
        state_dropdown = self.wait.until(
            EC.element_to_be_clickable((By.ID, "state"))
        )
        self.driver.execute_script("arguments[0].click();", state_dropdown)

        # Выбираем вариант из выпадающего списка
        state_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@id, 'state')]//div[text()='NCR']"))
        )
        state_option.click()
        print("✓ Выбран штат: NCR")

        # Заполняем поле City
        city_dropdown = self.wait.until(
            EC.element_to_be_clickable((By.ID, "city"))
        )
        self.driver.execute_script("arguments[0].click();", city_dropdown)

        # Выбираем город
        city_option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@id, 'city')]//div[text()='Delhi']"))
        )
        city_option.click()
        print("✓ Выбран город: Delhi")

        # Проверяем, что поля заполнены
        state_value = self.driver.find_element(By.ID, "state").find_element(By.CLASS_NAME, "css-1uccc91-singleValue")
        city_value = self.driver.find_element(By.ID, "city").find_element(By.CLASS_NAME, "css-1uccc91-singleValue")

        assert state_value.text == "NCR", f"Ожидался штат 'NCR', получен '{state_value.text}'"
        assert city_value.text == "Delhi", f"Ожидался город 'Delhi', получен '{city_value.text}'"

        print("✓ Поля State and City успешно заполнены")

        # Дополнительно: можно отправить форму
        submit_button = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].click();", submit_button)

        # Проверяем успешную отправку
        success_modal = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "modal-content"))
        )
        assert success_modal.is_displayed(), "Модальное окно успеха не отобразилось"
        print("✓ Форма успешно отправлена с выбранными State and City")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])