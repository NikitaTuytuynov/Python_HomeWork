# Задача 1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# - 6782 -> 23
# - 0.56 -> 11

# number = float(input('Введите число: '))
#
#
# def summa(num):
#     count = 0
#     num = str(num)
#     num = list(num)
#     for el in num:
#         if el != '.':
#             el = int(el)
#             count += el
#     return count
#
#
# result = summa(number)
# print(result)
# ------------------------------------------------------------------------------------------------------------------

# Задача 2
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# number = int(input('Введите число: '))
#
#
# def factorial(num):
#     res = 1
#     a = []
#     while res <= num:
#         factorial = 1
#         for i in range(2, res + 1):
#             factorial *= i
#         a.append(factorial)
#         res += 1
#     return a
#
#
# result = factorial(number)
# print(result)

# ------------------------------------------------------------------------------------------------------------------

# Задача 3
# Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.
# - Для n = 6: [2.0, 2.25, 2.37, 2.44, 2.488, 2.52]     ->       14.072    (Округлять не обязательно)

# number = int(input('Введите число: '))
#
#
# def summ(num):
#     count = 1
#     res = 0
#     a = []
#     while count <= num:
#         a.append((1 + 1 / count) ** count)
#         count += 1
#     for el in a:
#         res += el
#     return round(res, 3)
#
#
# result = summ(number)
# print(result)

# ------------------------------------------------------------------------------------------------------------------

# Задача 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.


# number = int(input('Введите число N: '))
# number_1 = int(input('Введите первый индекс: '))
# number_2 = int(input('Введите второй индекс: '))
#
#
# def array(num, first, second):
#     a = []
#     num_1 = - num
#     res = 0
#     while num_1 <= num:
#         a.append(num_1)
#         num_1 += 1
#     print(a)
#     res = a[first] * a[second]
#     return res
#
#
# result = array(number, number_1, number_2)
# print(result)




