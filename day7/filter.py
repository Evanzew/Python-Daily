# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 在一个list中，删掉偶数，只保留奇数，可以这么写：


def is_odd(n):
    return n % 2 == 1


print('list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))', list(
    filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# 把一个序列中的空字符串删掉，可以这么写：


def not_empty(s):
    return s and s.strip()


print("list(filter(not_empty, [' A ', '   ', ' B ', None, 'C', '  ']))", list(
    filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
