import numpy as np
import sympy as sp

def func(x, y):
    return (x + 2*y -7)**2 + (2*x + y - 5)**2 #Fungsi f(x, y) = (x + 2*y -7)**2 + (2*x + y - 5)**2

def funcDerivByX(x, y): #Turunan f(x) terhadap x biasa disebut g1
    return 10*x + 8*y - 34

def funcDerivByY(x, y): #Turunan f(x) terhadap y biasa disebut g2
    return 8*x + 10*y - 38

def findLearningRate(x, y):
    t = sp.Symbol("t")
    
    xVector = np.matrix([[x], [y]])
    gradientMatrix = np.matrix([[funcDerivByX(x, y)], [funcDerivByY(x, y)]])
    disambiguationFunction = xVector - t * gradientMatrix
    gradientTMatrix = np.matrix([[funcDerivByX(disambiguationFunction[0,0], disambiguationFunction[1,0])], [funcDerivByY(disambiguationFunction[0,0], disambiguationFunction[1,0])]]) 

    disambiguation = (- gradientTMatrix[0,0]) * gradientMatrix[0,0] + (- gradientTMatrix[1,0]) * gradientMatrix[1,0]

    return float(sp.solveset(disambiguation, t).args[0])

def steepest(x, y, n, t): #Method Newton dengan parameter x0, y0, banyak iterasi dan learning rate
    print(f"x0 = {x, y}, f(x0) = {func(x, y)}")
    for i in range(0, n):
        print(f"===Iterasi-{i + 1}=======================================================")
        xVector = np.matrix([[x], [y]]) #Vektor x yang adalah x, y
        gradientMatrix = np.matrix([[funcDerivByX(x, y)], [funcDerivByY(x, y)]]) #Gradien f(x) yang berisi turunan pertama f(x) terhadap x dan y
        xVectorNew = xVector - t * gradientMatrix #Rumus metode steepest descent untuk 2 variabel
        x = xVectorNew[0, 0]
        y = xVectorNew[1, 0]
        print(f"Gradient Matrix = {gradientMatrix.flatten()}")
        print(f"x{i + 1} = {x, y}, f(x{i+1}) = {func(x, y)}")
        print(f"Learning Rate: {t}")
        t = findLearningRate(x,y)
    print(f"Nilai Minimumnya adalah {func(x, y)}")

steepest(0, 0, 3, 0.25)