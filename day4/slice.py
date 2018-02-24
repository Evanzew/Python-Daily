L = ["colin", "herby", "andy", "chain", "evan"]

print("L[2:4]:", L[2:4])
print("L[-2:]:", L[-2:])
print("L[-2:-1]:", L[-2:-1])

L2 = list(range(100))
print("L2[:10]", L2[:10])
print("L2[-10:]", L2[-1:])
print("前十个每两个取一个 L2[:10:2]", L2[:10:2])
print("所有数每五个取一个 L2[::5]", L2[::5])

# 字符串和tuple也可以
print("'ABCDEFG'[:3]", 'ABCDEFG'[:3])
print("(0,1,2,3,4,5)[:3]", (0, 1, 2, 3, 4, 5)[:3])

# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：


def trim(s):
    start = 0
    end = -1
    while True:
        if s[start:start+1] == " ":
            start = start+1
        else:
            break

    while True:
        if s[end:] == " ":
            end = end-1
        else:
            break
    if end == -1:
        s = s[start:]
    else:
        s = s[start:end]
    return s


# 递归 这个牛逼


def trim2(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] == ' ':
        return trim2(s[1:])
    else:
        return trim2(s[:-1])


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!trim')

# 测试 trim2:
if trim2('hello  ') != 'hello':
    print('测试失败!')
elif trim2('  hello') != 'hello':
    print('测试失败!')
elif trim2('  hello  ') != 'hello':
    print('测试失败!')
elif trim2('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim2('') != '':
    print('测试失败!')
elif trim2('    ') != '':
    print('测试失败!')
else:
    print('测试成功!trim2')
