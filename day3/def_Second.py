def power(x, n=2):
    s = 1
    while n > 0:
        s = s*x
        n = n-1
    return s


def calc(*number):
    sum = 0
    for n in number:
        sum += n*n
    return sum


extra = {'city': 'Beijing', 'job': 'Engineer'}


def person(name, age, **kw):
    return ('name:', name, "age:", age, "other:", kw)


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


f1(1, 2)
f1(1, 2, 3, 4, 5, name="evan")


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f2(1, 2, 2, d="1", name="1")

print("power(4,1):", power(4, 1))
print("power(4):", power(4))
print("calc(1,2)", calc(1, 2))
print("calc(0)", calc(0))
print("person('evan',11,city='beijing')", person('evan', 11, city='beijing'))
print("person('Jack', 24, **extra):", person('Jack', 24, **extra))


def product(*number):
    sum = 1
    for n in number:
        sum = sum*n
    return sum


print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试成功')
    except TypeError:
        print('测试失败!')
