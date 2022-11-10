import numpy as np #Library Numpy

def func(x): #Fungsi f(x) = 4 * ln(x) - x
    return (4 * np.log(x)) - x

def derivFunc(x): #Fungsi turunan pertama f(x)
    return (4/x) - 1

def secondDerivFunc(x): #Fungsi turunan kedua f(x)
    return -4/(x**2)

def steepest(x, n, t): #Method steepest decsent dengan parameter x0, iterasi dan learning rate
    print(f"x0 = {x}, f(x) = {func(x)}")
    for i in range(0, n): #Melakukan perulangan untuk mendapat nilai x
        print(f"===Iterasi-{i+1}===============================")
        x = x - (t * derivFunc(x)) #Rumus Metode Steepest Descent
        print(f"x{i + 1} = {x}, f(x) = {func(x)}")
    print(f"Nilai Maximumnya adalah {func(x)}")

steepest(6, 3, 0.5)