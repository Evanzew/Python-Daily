def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


print(fact(1))
print(fact(10))


def first(n):
    return fact_ifter(n, 1)


def fact_ifter(num, product):
    if num == 1:
        return product
    else:
        return fact_ifter(num-1, num*product)


print(first(5))

# 汉诺塔


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')
