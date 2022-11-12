import numpy as np #Library Numpy

def func(x, y): #Fungsi f(x, y) = (x + 2*y -7)**2 + (2*x + y - 5)**2
    return (x + 2*y -7)**2 + (2*x + y - 5)**2

def funcDerivByX(x, y): #Turunan f(x) terhadap x disebut juga g1
    return 10*x + 8*y - 34

def funcDerivByY(x, y): #Turunan f(x) terhadap y disebut juga g1
    return 8*x + 10*y - 38

def funcG1DerivByX(x, y): #Turunan g1 terhadap x
    return 10

def funcG1DerivByY(x, y): #Turunan g1 terhadap y
    return 8

def funcG2DerivByX(x, y): #Turunan g2 terhadap x
    return 8

def funcG2DerivByY(x, y): #Turunan g2 terhadap y
    return 10

def newton(x, y, n): #Method Newton dengan parameter x0, y0 dan banyak iterasi
    print("Metode Newton:")
    print(f"x0 = {x, y}, f(x0) = {func(x, y)}")
    for i in range(0, n):
        print(f"===Iterasi-{i + 1}=======================================================")
        xVector = np.matrix([[x], [y]]) #Vektor x yang adalah x, y
        gradientMatrix = np.matrix([[round(funcDerivByX(x, y))], [round(funcDerivByY(x, y))]]) #Gradien f(x) yang berisi turunan pertama f(x) terhadap x dan y
        hessianMatrix = np.matrix([[funcG1DerivByX(x, y), funcG1DerivByY(x, y)], [funcG2DerivByX(x, y), funcG2DerivByY(x, y)]]) #Hessian f(x) (H f(x)) yang berisi turunan g1 dan g2 terhadap x dan y
        inverseHessianMatrix = np.linalg.inv(hessianMatrix) #Inverse dari hessian matrix (H^-1 f(x))
        xVectorNew = xVector - inverseHessianMatrix * gradientMatrix #Rumus metode newton untuk 2 variabel
        x = round(xVectorNew[0, 0])
        y = round(xVectorNew[1, 0])
        print(f"Gradient Matrix = {gradientMatrix.flatten()}")
        print(f"Hessian Matrix = {hessianMatrix.flatten()}")
        print(f"Inverse Hessian Matrix = {inverseHessianMatrix.flatten()}")
        print(f"x{i + 1} = {x,y}, f(x{i+1}) = {func(x, y)}")
    print(f"Nilai Minimumnya adalah {func(x, y)}")

newton(0, 0, 3)