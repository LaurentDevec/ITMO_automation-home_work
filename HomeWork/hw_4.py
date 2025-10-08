def find_max_number(num1, num2):
    if num1 > num2:
        print(num1)
    else:
        print(num2)

# 3. Функция на вход получает два произвольных числа. Вывести в консоль "yes", если они отличаются друг от друга на 135, иначе вывести на экран "No"
def check_difference(num1, num2):
    if abs(num1 - num2) == 135:
        print("yes")
    else:
        print("No")

# 4. Функция на вход получает произвольное число от 1 до 12 (номер месяца). Вывести название сезона года в консоль (зима, весна, лето, осень)
def get_season(month):
    if month in [12, 1, 2]:
        print("зима")
    elif month in [3, 4, 5]:
        print("весна")
    elif month in [6, 7, 8]:
        print("лето")
    elif month in [9, 10, 11]:
        print("осень")
    else:
        print("Неверный номер месяца")

# 5. Функция на вход получает три произвольных числа. Если все числа больше 10, то вывести на экран "yes", иначе "no"
def check_all_greater_than_ten(num1, num2, num3):
    if num1 > 10 and num2 > 10 and num3 > 10:
        print("yes")
    else:
        print("no")

# 6. Функция на вход получает список, состоящий из 5 произвольных чисел. Найти количество положительных чисел среди них.
def count_positive_numbers(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
        print(count)

# 7. Функция на вход получает 2 переменные: кол-во лет (int) и кол-во месяцев (int)
# Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.
def calculate_days(years, months):
    total_months = years * 12 + months
    total_days = total_months * 29
    print(total_days)

# Примеры использования функций:
    print("Задача 2:")
    find_max_number(5, 10)  # Выведет: 10
    find_max_number(-3, -1)  # Выведет: -1

    print("\nЗадача 3:")
    check_difference(100, 235)  # Выведет: yes
    check_difference(100, 200)  # Выведет: No

    print("\nЗадача 4:")
    get_season(7)  # Выведет: лето
    get_season(12)  # Выведет: зима

    print("\nЗадача 5:")
    check_all_greater_than_ten(15, 20, 25)  # Выведет: yes
    check_all_greater_than_ten(15, 5, 25)  # Выведет: no

    print("\nЗадача 6:")
    count_positive_numbers([-1, 2, -3, 4, 5])  # Выведет: 3
    count_positive_numbers([1, 2, 3, 4, 5])  # Выведет: 5
    count_positive_numbers([-1, -2, -3, -4, -5])  # Выведет: 0

    print("\nЗадача 7:")
    calculate_days(2, 3)  # Выведет: 783 (2 года * 12 месяцев + 3 месяца = 27 месяцев * 29 дней)
    calculate_days(0, 5)  # Выведет: 145 (5 месяцев * 29 дней)