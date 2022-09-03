# print ('введите первое число')
# a = int(input())
# print ('второе число2 первое число')
# b = int(input())

# if a==b**2 or b==a**2:
#  print ('да')
# else: print ('нет')

# numbers = []
# for _ in range(5):
#     n = int(input('Введите число: '))
#     numbers.append(n)

# maxx = numbers[0]
# for i in numbers:
#     if i > maxx:
#         maxx = i
# print(maxx)

# maxx = int(input('Введите число'))
# for _ in range(4):
#     n = int(input('Введите число: '))
#     if n > maxx:
#         maxx = n
# print(maxx)

# a = int(input('введите число: '))
# for i in range(-a, a+1):
#      print(f'{i}, ')

# a = int(input('введите число: '))
# if (a%5==0 and a%10==0 or a%15==0) and a%30!=0:
#     print('да')
# else:
#     print('нет')

# программа на вход принимает число N и выводит все числа от -N до N
# N=int(input('введите число '))
# for i in range(-N, N):
#     print(i, end=', ')
# print(N)

# программа принимает на вход дробь и показывает первую цифру дробной части числа
# первый вариант решения
# a = float(input('введите число '))
# if a%1 == 0:
#     print('нет')
# else:
#     print(int(a*10)%10)

#второй вариант решения
# a=input('введите число ')
# if '.' in a:
#     print(a[a.index('.')+1])
# elif ',' in a:
#     print(a[a.index(',')+1])
# else: 
#     print('нет')

# программа принимает число и проверяет кратно ли оно 5 и 10 или 15 но не 30
n = int(input('введите число '))
if (n%5==0 and n%10==0 or n%15==0) and n%30!=0:
    print('true')
else:
    print('false')



