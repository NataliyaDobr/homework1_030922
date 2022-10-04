# 1. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном
# списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

# from collections import Counter
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# ls = [i for i in src if src.count(i) == 1]
# print(ls)

# st_1 = list(set(src))

# ls_2 = [i for i in st_1 if src.count(i) == 1]
# print(ls_2)

# ls_3 = Counter(src)
# print(ls_3)

# a = set() #23 1 3 10 4 11
# b = set() #2 7 23 1 44 3 10 4 11
# for i in lst:
# if i not in b:
# a.add(i)
# else:
# a.discard(i)
# b.add(i)
# print(list(a))

# 2. Напишите программу, которая удаляет из строки все повтор символы
# s = input()
# s_final = ''
# set_s = list(set(s))
# s_final = ''.join(set_s)
# print(s_final)

# from curses.ascii import isdigit


# print(''.join(list(set(input()))))

# 3. Напишите программу, которая находит все цифры, которых нет в переданной ей строке
# s_dij = '9876543210'
# s = input('Введите строку ')
# dij_set = set()
# for i in s:
#     if i.isdigit():
#         dij_set.add(i)

# print(dij_set)
# s_final = ''
# for i in s_dij:
#     if i not in dij_set:
#         s_final+= i

# if s_final:
#     print(s_final)
# else:
#     print('No')

# s = input()
# res = ''.join(str(i) for i in range(10)[::-1] if str(i) not in s)
# print(res if res else 'NO')

# 4. Напишите программу, котороая вводит две символьные строки и находит все латинские буквы 
# которых нет не в одной из этих строк. Заглавные и строчные не различаются
