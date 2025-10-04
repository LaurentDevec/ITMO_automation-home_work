def task_1() -> None:
    """
    Функция создает 5 переменных разных типов и выводит их типы в консоль.
    """
    # Создание переменных разных типов
    integer_number = 42  # int
    float_number = 3.14  # float
    text_string = "Hello, World!"  # str
    number_list = [1, 2, 3, 4, 5]  # list
    boolean_value = True  # bool

    # Вывод типов данных в консоль
    print("=== ЗАДАЧА 1 ===")
    print(f"Тип переменной integer_number: {type(integer_number)}")
    print(f"Тип переменной float_number: {type(float_number)}")
    print(f"Тип переменной text_string: {type(text_string)}")
    print(f"Тип переменной number_list: {type(number_list)}")
    print(f"Тип переменной boolean_value: {type(boolean_value)}")
    print()


# Задача 2
def task_2() -> None:
    """
    Функция выводит первые 3 значения списка чисел.
    """
    # Создание списка
    a = [1, 2, 3, 5, 8, 13, 21]

    # Вывод первых 3 значений
    print("=== ЗАДАЧА 2 ===")
    print("Полный список:", a)
    print("Первые 3 значения списка:", a[:3])
    print("Эта последовательность чисел называется: Числа Фибоначчи")
    print()



