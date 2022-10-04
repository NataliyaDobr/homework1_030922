# 1. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Пример:
# some_list = [int(input('Введите строку ')) for _ in range(int(input('введите число ')))]
# print(some_list)
# new_list = some_list[::-1]
# print(new_list)
# result = [some_list[i]*new_list[i] for i in range(round(len(some_list)/2)) ]
# print(result)

# 2. задайте строку из набора чисел. напишите программу, которая покажет большее и меньшее число.
# def select (f,col):
#     return[f(x) for x in col]

# def where (f,col):
#     return[x for x in col if f(x)]

# data = '1 2 25 988 36'.split()
# res = select(int, data)
# res_max = where (lambda x: x==max(res), res)
# res_min = where (lambda x: x==min(res), res)
# print(res_max, res_min)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
some_list = [1.1, 1.2, 3.1, 5, 10.01]
fract_part = [some_list[i]-int(some_list[i]) for i in range(len(some_list))]
print(max(fract_part)-min(fract_part))

