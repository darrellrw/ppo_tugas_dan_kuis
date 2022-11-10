import numpy as np

def func(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 -7)**2

def funcDerivByX(x, y):
    return 4*x**3 + 4*x*y - 42*x + 2*y**2 - 14

def funcDerivByY(x, y):
    return -26*y + 2*x**2 - 22 + 4*y**3 + 4*x*y

def funcG1DerivByX(x, y):
    return 12*x**2 + 4*y - 42

def funcG1DerivByY(x, y):
    return 4*x + 4*y

def funcG2DerivByX(x, y):
    return 4*x + 4*y

def funcG2DerivByY(x, y):
    return -26 + 12*y**2 + 4*x

def steepest(x, y, t):
    print(f"x0 = ({x}, {y}), f(x) = {func(x, y)}")
    for i in range(0, len(t)):
        xVector = np.matrix([[x], [y]])
        gradientMatrix = np.matrix([[funcDerivByX(x, y)], [funcDerivByY(x, y)]])
        xVectorNew = xVector - t[i] * gradientMatrix
        x = xVectorNew[0, 0]
        y = xVectorNew[1, 0]
        print(f"x{i + 1} = ({x}, {y}), f(x) = {func(x, y)}")
    print(f"Nilai Maximumnya adalah {func(x, y)}")

steepest(5, 5, [1, 0.5, 0.5])