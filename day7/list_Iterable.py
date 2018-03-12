# 直接作用于for循环的对象统称为可迭代对象：Iterable,可以使用isinstance()判断一个对象是否是Iterable对象：

from collections import Iterable
print("isinstance([],Iterable)", isinstance([], Iterable))
print("isinstance({},Iterable)", isinstance({}, Iterable))
print("isinstance('abc', Iterable)", isinstance('abc', Iterable))
print("isinstance((x for x in range(10)), Iterable)",
      isinstance((x for x in range(10)), Iterable))
print("isinstance(100, Iterable)", isinstance(100, Iterable))

# 可以被next()函数调用并不断返回下一个值的对象成为迭代器：Iterator，可以使用isinstance()判断一个对象是否是Inerator对象：

from collections import Iterator
print("isinstance((x for x in range(10)), Iterator)",
      isinstance((x for x in range(10)), Iterator))
print("isinstance([], Iterator)", isinstance([], Iterator))
print("isinstance({}, Iterator)", isinstance({}, Iterator))
print("isinstance('abc', Iterator)", isinstance('abc', Iterator))

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print("isinstance(iter([]), Iterator)", isinstance(iter([]), Iterator))
print("isinstance(iter('abc'), Iterator)", isinstance(iter('abc'), Iterator))
