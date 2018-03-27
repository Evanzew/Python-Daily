# 1.map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator


def f(x):
    return x*x


print("list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))",
      list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

print("list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))",
      list(map(int,  ['1', '2', '3', '4', '5', '6', '7', '8', '9'])))

# 2.reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce


def add(x, y):
    return x+y


print("reduce(add, [1, 2, 3, 4, 5])", reduce(add, [1, 2, 3, 4, 5]))


def fn(x, y):
    return x*10+y


print("reduce(fn, [1, 3, 5, 7, 9]),", reduce(fn, [1, 3, 5, 7, 9]))

# 练习1：利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：


def normalize(name):
    return name[0].uper()+name[1:].lower()

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：


def prod(L):
    if(len(L) == 1):
        return L[0]
    else:
        return reduce(lambda x, y: x*y, L)

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：


def str2float(s):
    s = s.split('.')

    def mul(x, y):
        return x*10+y
    return reduce(mul, map(int, s[0]))+reduce(mul, map(int, s[1]))/(10 ** len(s[1]))
