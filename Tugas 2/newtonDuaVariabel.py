import numpy as np

def func(x, y): #Fungsi f(x) (x**2 + y - 11)**2 + (x + y**2 -7)**2
    return (x**2 + y - 11)**2 + (x + y**2 -7)**2

def funcDerivByX(x, y): #Fungsi turunan f(x) terhadap x disebut juga g1
    return 4*x**3 + 4*x*y - 42*x + 2*y**2 - 14

def funcDerivByY(x, y): #Fungsi turunan f(x) terhadap y disebut juga g2
    return -26*y + 2*x**2 - 22 + 4*y**3 + 4*x*y

def funcG1DerivByX(x, y): #Fungsi turunan g1 terhadap x
    return 12*x**2 + 4*y - 42

def funcG1DerivByY(x, y): #Fungsi turunan g1 terhadap y
    return 4*x + 4*y

def funcG2DerivByX(x, y): #Fungsi turunan g2 terhadap x
    return 4*x + 4*y

def funcG2DerivByY(x, y): #Fungsi turunan g2 terhadap y
    return -26 + 12*y**2 + 4*x

def newton(x, y, n):
    print(f"x0 = ({x}, {y}), f(x) = {func(x, y)}")
    for i in range(0, n):
        xVector = np.matrix([[x], [y]])
        gradientMatrix = np.matrix([[funcDerivByX(x, y)], [funcDerivByY(x, y)]])
        hessianMatrix = np.matrix([[funcG1DerivByX(x, y), funcG1DerivByY(x, y)], [funcG2DerivByX(x, y), funcG2DerivByY(x, y)]])
        inverseHessianMatrix = np.linalg.inv(hessianMatrix)
        xVectorNew = xVector - inverseHessianMatrix * gradientMatrix
        x = xVectorNew[0, 0]
        y = xVectorNew[1, 0]
        print(f"x{i + 1} = ({x}, {y}), f(x) = {func(x, y)}")
    print(f"Nilai Minimumnya adalah {func(x, y)}")

newton(5, 5, 3)