import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginFormValidate:

    @pytest.fixture(autouse=True)
    def setup(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()

    def test_placeholder_validation(self):

        self.driver.get("https://demoqa.com/automation-practice-form")



        first_name_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "firstName"))
        )
        first_name_placeholder = first_name_input.get_attribute("placeholder")
        expected_first_name_placeholder = "First Name"
        assert first_name_placeholder == expected_first_name_placeholder, \
            f"Плейсхолдер First Name: ожидалось '{expected_first_name_placeholder}', получено '{first_name_placeholder}'"
        print(f"✓ Плейсхолдер First Name: {first_name_placeholder}")


        last_name_input = self.driver.find_element(By.ID, "lastName")
        last_name_placeholder = last_name_input.get_attribute("placeholder")
        expected_last_name_placeholder = "Last Name"
        assert last_name_placeholder == expected_last_name_placeholder, \
            f"Плейсхолдер Last Name: ожидалось '{expected_last_name_placeholder}', получено '{last_name_placeholder}'"
        print(f"✓ Плейсхолдер Last Name: {last_name_placeholder}")

        user_email_input = self.driver.find_element(By.ID, "userEmail")
        user_email_placeholder = user_email_input.get_attribute("placeholder")
        expected_email_placeholder = "name@example.com"
        assert user_email_placeholder == expected_email_placeholder, \
            f"Плейсхолдер Email: ожидалось '{expected_email_placeholder}', получено '{user_email_placeholder}'"
        print(f"✓ Плейсхолдер Email: {user_email_placeholder}")

        # Проверка атрибута pattern для email
        email_pattern = user_email_input.get_attribute("pattern")
        expected_pattern = ".+@.+\..+"

        if email_pattern:
            assert email_pattern == expected_pattern, \
                f"Pattern email: ожидалось '{expected_pattern}', получено '{email_pattern}'"
            print(f"✓ Pattern атрибут email: {email_pattern}")
        else:
            print("✓ Pattern атрибут не установлен для email поля")

    def test_empty_form_validation(self):
        """Тест валидации пустой формы"""

        self.driver.get("https://demoqa.com/automation-practice-form")

        form = self.wait.until(
            EC.presence_of_element_located((By.ID, "userForm"))
        )

        assert "was-validated" not in form.get_attribute("class"), \
            "Класс 'was-validated' не должен присутствовать до отправки формы"

        submit_button = self.driver.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()

        form_after_submit = self.driver.find_element(By.ID, "userForm")
        form_class = form_after_submit.get_attribute("class")

        assert "was-validated" in form_class, \
            f"Класс 'was-validated' не найден в форме после отправки. Классы формы: {form_class}"

        print("✓ Форма получила класс 'was-validated' после попытки отправки пустой формы")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])