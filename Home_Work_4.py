import math

# 1 Вычислить число π c заданной точностью d
# - при $d = 0.001, π = 3.141.$


# number = float(input('Введите число: '))
#
#
# def pi(num):
#     a = 6 * math.atan(1 / math.sqrt(3))
#     res = (a - math.pi)
#     if res < num:
#         return  a
#
#
# result = pi(number)
# print("π = ", result)

# ------------------------------------------------------------------------------------------------------------------------
# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# - при N=236 -> [2, 2, 59]


# number = int(input('Введите число: '))
#
#
# def digit(num):
#     a = []
#     b = 0
#     n = 0
#     while num > 1:
#         b = 2
#         n = num
#         while n == num:
#             if num % b == 0:
#                 a.append(b)
#                 num /= b
#             else:
#                 b += 1
#     return a
#
#
# res = digit(number)
# print(res)

# ------------------------------------------------------------------------------------------------------------------------
# 3 Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

# array = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
#
#
# def ar(arr):
#     i = 0
#     b = []
#     while i < len(arr):
#         if arr.count(arr[i]) > 1:
#             i += 1
#         else:
#             b.append(arr[i])
#             i += 1
#     return b
#
#
# res = ar(array)
# print(res)
# ------------------------------------------------------------------------------------------------------------------------


import random

# x = int(input('Введите число: '))
# a = []
# b = ['+', '-']
# i = 0
# c = 0
# e = x
# s = x
# j = random.randrange(0, 100)
# while i < x:
#     c = random.randint(0, 3)
#     if c != 0:
#         if e != 0 and e != 1:
#             a.append(f' {random.randrange(1, 100)}x^{e} {random.choice(b)}')
#             i += 1
#             e = e - 1
#         elif e == 1:
#             a.append(f' {random.randrange(1, 100)}x {random.choice(b)}')
#             i += 1
#             e = e - 1
#         else:
#             i += 1
#     else:
#         i += 1
# if len(a) == 0:
#     a.append(f'{random.randrange(1, 100)}x^{s} {random.choice(b)}')
# if j != 0:
#     a.append(f' {j} = 0')
# else:
#     a.append('= 0')
#
# a = ("".join(a))
#
# data = open('homework4.txt', 'w')
# data.write(a)
# data.close