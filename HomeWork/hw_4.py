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
        print(f"Умножение: {self.a} * {self.b} = {result}")
        return result

    def division(self):
        if self.b != 0:
            result = self.a / self.b
            print(f"Деление: {self.a} / {self.b} = {result}")
            return result
        else:
            print("Ошибка: деление на ноль!")
            return None

    def subtraction(self):
        result = self.a - self.b
        print(f"Вычитание: {self.a} - {self.b} = {result}")
        return result