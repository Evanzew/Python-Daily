# generator 初步创建,一边循环一边计算,可以节约内存

g = (x*x for x in range(10))
print(g)

# 创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误
print(next(g))
for n in g:
    print(n)

# 斐波那契函数:非generator


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    print("done")


fib(6)

# 斐波那契函数:generator


def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
    return 'done'


f = fib_generator(6)

# 1.不拿return后的值
for value in f:
    print(value)

# 2.拿return后的值

g = fib_generator(6)
while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as e:
        print(e.value)
        break

# 杨辉三角


def triangles_complicated():
    L1 = [1]
    yield L1
    while True:
        a, b = 0, 0
        L = []
        for n in L1:
            a, b = n, a
            L.append(a+b)
        L.append(a)
        L1 = L
        yield L1

# 简洁版杨辉三角


def triangles():
    L = [1]
    while True:
        yield L
        L = [1]+[L[n] + L[n+1] for n in range(len(L)-1)]+[1]


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
