import numpy as np #Library Numpy
import random

def func(x): #Fungsi f(x) = ln(x**2 + 1)
    return np.log(x**2 + 1)

class SwarmMethod: #Kelas Metode PSO
    def __init__(self, x, v, c, r, w): #Inisisasi x0 v c r w
        self.x = x
        self.v = []
        self.c = c
        self.r = r
        self.w = w
        self.f = []
        self.gBest = None
        self.pBest = []
        self.oldX = []
        for i in range(0, len(x)):
            self.v.append(v)
            self.f.append(None)
            self.pBest.append(None)
            self.oldX.append(None)
    
    def swarm(self, n): #Method PSO
        #Step 1 Menentukan x dan v
        def particle(x, v): #Method untuk menentukan partikel
            for i in range(len(x)):
                self.x[i] = x[i]
            for i in range(len(v)):
                self.v[i] = v[i]

        #Step 2 Menentukan Nilai fungsi f(x)
        def mencariNilaiFungsi(): #Method untuk mencari nilai fungsi
            for i in range(len(self.f)):
                self.f[i] = func(self.x[i])
        
        #Step 3 Menentukan gBest
        def gBest(): #Method untuk mencari gBest
            self.gBest = self.x[self.f.index(min(self.f))]

        #Step 4 Menentukan pBest
        def pBest(): #Method untuk mencari pBest
            if(self.pBest[0] == None):
                for i in range(len(self.x)):
                    self.pBest[i] = self.x[i]
            else:
                for i in range(len(self.x)):
                    if(func(self.oldX[i]) >= self.f[i]):
                        self.pBest[i] = self.x[i]
                    else:
                        self.pBest[i] = self.oldX[i]

        #Step 5 Memperbarui v
        def updateV(): #Method untuk mengupdate nilai v
            for i in range(len(self.v)):
                self.v[i] = self.w * self.v[i] + self.c[0] * self.r[0] * (self.pBest[i] - self.x[i]) + self.c[1] * self.r[1] * (self.gBest - self.x[i])
        
        #Step 6 Memperbarui x
        def updateX(): #Method untuk mengupdate nilai x
            for i in range(len(self.x)):
                self.oldX[i] = self.x[i]
                self.x[i] = self.x[i] + self.v[i]

        for i in range(0, n): #Perulangan untuk mendapat nilai x
            particle(self.x, self.v)
            mencariNilaiFungsi()
            gBest()
            pBest()
            updateV()
            updateX()
            print(f"===Iterasi-{i + 1}=======================================================")
            print("Sebelum:", end=" ")
            for i in range(0, len(x)):
                if(i == len(x) - 1):
                    print(f"x{i} = {self.oldX[i]}", end="\n")
                else:
                    print(f"x{i} = {self.oldX[i]}", end=", ")
            print(f"gBest = {self.gBest}")
            print(f"pBest = {self.pBest}")
            print(f"v = {self.v}")
            print("Sesudah:", end=" ")
            for i in range(0, len(x)):
                if(i == len(x) - 1):
                    print(f"x{i} = {self.x[i]}", end="\n")
                else:
                    print(f"x{i} = {self.x[i]}", end=", ")
            print("Nilai Fungsi:", end=" ")
            for i in range(0, len(x)):
                if(i == len(x) - 1):
                    print(f"x{i} = {self.f[i]}", end="\n")
                else:
                    print(f"x{i} = {self.f[i]}", end=", ")

x = np.random.randint(-10, 10, size=10)
r = np.random.rand(2)
print(f"Nilai Random x: {x}")
print(f"Nilai Random r: {r}")
sm = SwarmMethod(x, 0, [0.5, 1], r, 1)
sm.swarm(3)