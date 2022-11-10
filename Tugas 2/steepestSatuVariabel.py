from math import *

def func(x):
    return (4 * log(x)) - x

def derivFunc(x):
    return (4/x) - 1

def secondDerivFunc(x):
    return -4/(x**2)

def steepest(x, n, t):
    print(f"x0 = {x}")
    for i in range(0, n):
        x = x - (t * derivFunc(x))
        print(f"x{i + 1} = {x}")
    print(f"Nilai Maximumnya adalah {func(x)}")

steepest(6, 3, 0.5)