# 1 Напишите программу, удаляющую из файла все слова, содержащие "абв".

# f = open('text_1.txt', encoding="utf-8")
# data = f.read()
# f.close()
# lis = data.split(' ')
# res = []
# i = 0
# while i < len(lis):
#     if lis[i].count('а') >= 1 and lis[i].count('б') >= 1 and lis[i].count('в') >= 1:
#         res.append(lis[i])
#     i += 1
# result = [i for i in lis if i not in res]
# result = (" ".join(result))
# data = open('text_1.txt', 'a',encoding="utf-8")
# data.write('\n' + result)
# data.close()
# ------------------------------------------------------------------------------------------------------------------------
# 2 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

# from random import randint
#
# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x
#
#
# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")
#
# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2)
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
#
# counter1 = 0
# counter2 = 0
#
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
#
# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

# ------------------------------------------------------------------------------------------------------------------------
# 3 Создайте программу для игры в "Крестики-нолики".


# a = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
# print(f'{a[0]} | {a[1]} | {a[2]}')
# print('---------')
# print(f'{a[3]} | {a[4]} | {a[5]}')
# print('---------')
# print(f'{a[6]} | {a[7]} | {a[8]}')
#
# i = 0
# while i < len(a):
#     if i == 0 or i % 2 == 0:
#         number = int(input('Введите номер сектора куда поставить Х: '))
#         if a[number-1] != '0' and a[number-1] != 'X':
#             a[number- 1] = 'X'
#             print(f'{a[0]} | {a[1]} | {a[2]}')
#             print('---------')
#             print(f'{a[3]} | {a[4]} | {a[5]}')
#             print('---------')
#             print(f'{a[6]} | {a[7]} | {a[8]}')
#             i += 1
#             if (a[0] == a[1] == a[2] == 'X') or (a[3] == a[4] == a[5] == 'X') or (a[6] == a[7] == a[8] == 'X') or (
#                     a[0] == a[3] == a[6] == 'X') or (a[1] == a[4] == a[7] == 'X') or (a[2] == a[5] == a[8] == 'X') or (
#                     a[0] == a[4] == a[8] == 'X') or (a[2] == a[4] == a[6] == 'X'):
#                 print('Победа X, поздавляем!!!')
#                 break
#         else:
#             print('Ошибка, тут уже стоит X или 0')
#             break
#     else:
#         number = int(input('Введите номер сектора куда поставить 0: '))
#         if a[number - 1] != 'X' and a[number-1] != '0':
#             a[number - 1] = '0'
#             print(f'{a[0]} | {a[1]} | {a[2]}')
#             print('---------')
#             print(f'{a[3]} | {a[4]} | {a[5]}')
#             print('---------')
#             print(f'{a[6]} | {a[7]} | {a[8]}')
#             i += 1
#             if (a[0] == a[1] == a[2] == '0') or (a[3] == a[4] == a[5] == '0') or (a[6] == a[7] == a[8] == '0') or (
#                     a[0] == a[3] == a[6] == '0') or (a[1] == a[4] == a[7] == '0') or (a[2] == a[5] == a[8] == '0') or (
#                     a[0] == a[4] == a[8] == '0') or (a[2] == a[4] == a[6] == '0'):
#                 print('')
#                 print('Победа 0, поздавляем!!!')
#                 break
#         else:
#             print('Ошибка, тут уже стоит X или 0')
#             break

# ------------------------------------------------------------------------------------------------------------------------
# 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
# 4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff
f = open('text_4.1.txt','r')
input1 = f.read()
f.close()

def archive(res):
    res = list(res)
    a = []
    b = []
    j = 0
    d = 0
    n = 0
    s = 9
    k = 0
    while j < len(res):
        k = 0
        i = res.count(res[j])
        if i < 10:
            res[j] = [f'{i}{res[j]}']
            j += i
        else:
            n = i // s
            while k < n:
                res[j] = [f'{9}{res[j]}']
                j += s
                k += 1
            res[j] = [f'{i - s * n}{res[j]}']
            j += (i - s * n)
    for el in res:
        if type(el) == list:
            a.append(el)
    while d < len(a):
        b.append(a[d][0])
        d+=1
    b = ("".join(b))
    return b

def unzipping(res):
    res = list(res)
    for i in range(len(res)):
        if i == 0 or i % 2 == 0:
            res[i] = int(res[i])
        else:
            res[i] *= res[i - 1]
    for el in res:
        if type(el) == int:
            res.remove(el)
    res = ("".join(res))
    return res

num = int(input('Выберете действие: нажмите 1 для архивации, нажмите 2 для разархивации: '))
if num == 1:
    result = archive(input1)
    f = open('text_4.2.txt', 'w')
    f.write(result)
    print('Результат записан в файл text_4.2.txt')
    f.close()
if num == 2:
    result = unzipping(input1)
    f = open('text_4.2.txt', 'w')
    f.write(result)
    print('Результат записан в файл text_4.2.txt')
    f.close()
# ------------------------------------------------------------------------------------------------------------------------
# 5* Дан список чисел. Найдите все возрастающие последовательности. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

