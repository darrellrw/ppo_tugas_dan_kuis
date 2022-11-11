import numpy as np #Library Numpy

def func(x): #Fungsi f(x) = ln(x**2 + 1)
    return np.log(x**2 + 1)

def derivFunc(x): #Fungsi turunan pertama f(x)
    return (2*x) / (x**2 + 1)

def secondDerivFunc(x): #Fungsi turunan kedua f(x)
    return (2 - 2*x**2) / (x**4 + 2*x**2 + 1)

def newton(x, n): #Method Newton dengan parameter x0 dan banyak iterasi
    print(f"x0 = {x}, f(x) = {func(x)}")
    for i in range(0, n): #Melakukan perulangan untuk mendapat nilai x
        print(f"===Iterasi-{i+1}===============================")
        x = x - (derivFunc(x) / secondDerivFunc(x)) #Rumus Metode Newton
        print(f"x{i + 1} = {x}, f(x) = {func(x)}")
    print(f"Nilai Maximumnya adalah {func(x)}")

newton(2, 3)