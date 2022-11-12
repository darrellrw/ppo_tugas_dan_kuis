import numpy as np #Library Numpy

def func(x): #Fungsi f(x) = ln(x**2 + 1)
    return np.log(x**2 + 1)

def derivFunc(x): #Fungsi turunan pertama f(x)
    return (2*x) / (x**2 + 1)

def steepest(x, n, t): #Method steepest decsent dengan parameter x0, iterasi dan learning rate
    print("Metode Steepest Descent:")
    print(f"x0 = {x}, f(x) = {func(x)}")
    for i in range(0, n): #Melakukan perulangan untuk mendapat nilai x
        print(f"===Iterasi-{i+1}===============================")
        x = x - (t * derivFunc(x)) #Rumus Metode Steepest Descent
        print(f"x{i + 1} = {x}, f(x) = {func(x)}")
    print(f"Nilai Maximumnya adalah {func(x)}")

steepest(1, 3, 0.25)