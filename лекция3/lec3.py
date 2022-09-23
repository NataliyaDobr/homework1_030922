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
def f(x):
    return x**3

list = [(i,f(i)) for i in range(1,21) if i%2==0]
print(list)