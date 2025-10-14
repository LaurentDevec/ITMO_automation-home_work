from task_9_checks import Checks

class Buttons(Checks):
    def __init__(self, loc):
        super().__init__(loc)

class Input(Checks):
    def __init__(self, loc):
        super().__init__(loc)

class Title(Checks):
    def __init__(self, loc):
        super().__init__(loc)

class Link(Checks):
    def __init__(self, loc):
        super().__init__(loc)

# Создание объектов и вызов метода check_text()
search = Buttons('Кнопка поиска')
search_field = Input('Поле поиска')
main_title = Title('Главный заголовок')
main_link = Link('Главная ссылка')

# Вывод результатов
print(search.check_text())
print(search_field.check_text())
print(main_title.check_text())
print(main_link.check_text())