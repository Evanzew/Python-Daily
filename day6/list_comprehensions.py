# 生成 1-10
print("list(range(1,11))", list(range(1, 11)))

# for 循环生成 [1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1, 11):
    L.append(x*x)
print(L)

# 列表生成时代替上述循环
[x * x for x in range(1, 11)]
print("[x * x for x in range(1, 11)]", [x*x for x in range(1, 11)])

# for循环后加上if判断
[x*x for x in range(1, 11) if x % 2 == 0]
print("[x*x for x in range(1, 11) if x % 2 == 0]",
      [x*x for x in range(1, 11) if x % 2 == 0])

# for两层循环
print("[m + n for m in 'ABC' for n in 'XYZ']",
      [m + n for m in "ABC" for n in "XYZ"])

# 列上级目录下所有的文件和目录名
import os
print("[d for d in os.listdir('../')]", [d for d in os.listdir('../')])

# 循环多个变量
double = {'x': 'A', 'y': 'B', 'z': 'C'}
print("[k+'+'+v for k, v in double.items()]",
      [k+"+"+v.lower() for k, v in double.items()])

# 通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)
