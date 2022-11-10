import numpy as np

def func(x):
    return (4 * np.log(x)) - x

def derivFunc(x):
    return (4/x) - 1

def secondDerivFunc(x):
    return -4/(x**2)

def newton(x, n):
    print(f"x0 = {x}")
    for i in range(0, n):
        x = x - (derivFunc(x) / secondDerivFunc(x))
        print(f"x{i + 1} = {x}")
    print(f"Nilai Maximumnya adalah {func(x)}")

newton(6, 3)