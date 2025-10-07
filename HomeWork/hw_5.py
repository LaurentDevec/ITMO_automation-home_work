from selene import browser, have, be
import time


def test_saucedemo_login():
    """Функция для проверки элементов на странице Saucedemo"""

    # a. Переходим на страницу
    browser.open('https://www.saucedemo.com/')

    # b. Находим элементы
    username_field = browser.element('#user-name')
    password_field = browser.element('#password')
    submit_button = browser.element('#login-button')

    # c. Проверяем, что элементы найдены
    if username_field.matching(be.visible) and password_field.matching(be.visible) and submit_button.matching(
            be.visible):
        print("Элементы найдены")

        # Дополнительно: проверяем плейсхолдеры
        username_field.should(have.attribute('placeholder').value('Username'))
        password_field.should(have.attribute('placeholder').value('Password'))
        submit_button.should(have.attribute('value').value('Login'))

        print("Все элементы корректно отображаются")
    else:
        print("Не все элементы найдены")

    # Закрываем браузер
    browser.quit()


# Запуск функции
if __name__ == "__main__":
    test_saucedemo_login()