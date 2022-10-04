# def f(x):
#     return x**2
# g = f

# print(f(4))
# print(g(4))

# def calc(x):
#     return x+10
# #print(calc(10))

# def calc2(x):
#     return x*10
# #print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2,10)
# math(calc,10)

# def mult(x, y):
#     return x*y

# def calc(op, a, b):
#     print(op(a,b))
#     #return op(a,b)

# calc(lambda x,y: x+y, 4, 5)

# List Comprehension
# чтобы быстро создавать списки
# список четных чисел в диапазоне от 1 до 100
# def f(x):
#     return x**3

# list = [(i,f(i)) for i in range(1,21) if i%2==0]
# print(list)

# анонимные lambda функции
# def select (f,col):
#     return[f(x) for x in col]

# def where (f,col):
#     return[x for x in col if f(x)]

# data = '1 2 3 4 5 8 15 23 38'.split()

# res = select(int, data)
# res = where (lambda x: not x%2, res)
# res = select(lambda x: (x,x**2) ,res)
# print(res)

# функция map
# li = [x for x in range(1,20)]
# li = list(map(lambda x:x+10, li))
# print(li)

# data = list(map(int,'1 2 3 4 555'.split()))
# for e in data:
#    print(e)

# функция FILTER
# data = [x for x in range(10)]
# res = list(filter(lambda x: x%2==0, data))
# print(res)

# функция ZIP - создает кортеж из 2 списков
# функция enumerate - нумерует объекты списка
