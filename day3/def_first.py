import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x+step*math.cos(angle)
    ny = y-step*math.sin(angle)
    return nx, ny


def quadratic(a, b, c):
    x = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    y = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x, y


x, y = move(100, 100, 60, math.pi/6)
print(my_abs(-99))
print(x, y)
print("type:", type(move(100, 100, 60, math.pi/6)))
