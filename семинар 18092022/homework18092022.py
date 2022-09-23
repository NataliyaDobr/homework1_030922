# 1. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Пример:
some_list = [int(input('Введите строку ')) for _ in range(int(input('введите число ')))]
print(some_list)
new_list = some_list[::-1]
print(new_list)
result = [some_list[i]*new_list[i] for i in range(round(len(some_list)/2)) ]
print(result)