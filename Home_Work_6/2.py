# 3
# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]
# было:
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
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------

# стало:
array = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
array = [i for i in array if array.count(i) == 1]
print(array)