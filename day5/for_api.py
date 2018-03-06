# 判断是否可迭代 Iterable
from collections import Iterable

print("isinstance('123',Iterable)", isinstance("123", Iterable))
print("isinstance([1,2,3],Iterable)", isinstance([1, 2, 3], Iterable))
print("isinstance(123,Iterable)", isinstance(123, Iterable))

# 带下标的遍历 enumerate

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 3), (3, 4)]:
    print(x, y)


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    else:
        max = min = L[0]
        for key in L:
            if key > max:
                max = key
            if key < min:
                min = key
    return (min, max)


if findMinAndMax([]) != (None, None):
    print(['测试失败!'])
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
