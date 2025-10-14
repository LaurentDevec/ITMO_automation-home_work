class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


# Создание объектов и расчеты
rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)
rect3 = Rectangle(8, 12)

print("Прямоугольник 1:")
print(f"Площадь: {rect1.calculate_area()}")
print(f"Периметр: {rect1.calculate_perimeter()}\n")

print("Прямоугольник 2:")
print(f"Площадь: {rect2.calculate_area()}")
print(f"Периметр: {rect2.calculate_perimeter()}\n")

print("Прямоугольник 3:")
print(f"Площадь: {rect3.calculate_area()}")
print(f"Периметр: {rect3.calculate_perimeter()}")


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        result = self.a + self.b
        print(f"Сложение: {self.a} + {self.b} = {result}")
        return result

    def multiplication(self):
        result = self.a * self.b
        print(f"Умножение: {self.a} × {self.b} = {result}")
        return result

    def division(self):
        if self.b == 0:
            print("Ошибка: деление на ноль!")
            return None
        result = self.a / self.b
        print(f"Деление: {self.a} ÷ {self.b} = {result}")
        return result

    def subtraction(self):
        result = self.a - self.b
        print(f"Вычитание: {self.a} - {self.b} = {result}")
        return result

class SidebarButton:
    def __init__(self, button_text):
        self.text = button_text
        self.type = "Кнопка"
        self.locator = ""

    def click(self):
        return f"Клик по кнопке {{{self.text}}}"

# Создание объектов для кнопок
buttons_data = [
    "Text Box", "Check Box", "Radio Button", "Web Tables",
    "Buttons", "Links", "Broken Links - Images",
    "Upload and Download", "Dynamic Properties"
]

buttons = [SidebarButton(text) for text in buttons_data]

# Вывод текста и клики
for button in buttons:
    print(f"Текст кнопки: {button.text}")
    print(f"Тип: {button.type}")
    print(f"Локатор: {button.locator}")
    print(button.click())
    print("---")


class Car:
    def __init__(self, color="", type="", year=""):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year
        print(f"Год выпуска установлен: {year}")

    def set_type(self, type):
        self.type = type
        print(f"Тип автомобиля установлен: {type}")

    def set_color(self, color):
        self.color = color
        print(f"Цвет автомобиля установлен: {color}")

    def get_info(self):
        return f"Автомобиль: {self.color} {self.type} {self.year} года"


# Пример использования
if __name__ == "__main__":
    my_car = Car()
    my_car.set_color("Красный")
    my_car.set_type("Седан")
    my_car.set_year(2022)
    my_car.start()
    print(my_car.get_info())
    my_car.stop()


