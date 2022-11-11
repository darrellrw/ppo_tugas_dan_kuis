import numpy as np #Library Numpy

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
        def particle(x, v): #Method untuk menentukan partikel
            for i in range(len(x)):
                self.x[i] = x[i]
            for i in range(len(v)):
                self.v[i] = v[i]
        def mencariNilaiFungsi(): #Method untuk mencari nilai fungsi
            for i in range(len(self.f)):
                self.f[i] = func(self.x[i])
        def gBest(): #Method untuk mencari gBest
            self.gBest = self.x[self.f.index(min(self.f))]
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
        def updateV(): #Method untuk mengupdate nilai v
            for i in range(len(self.v)):
                self.v[i] = self.w * self.v[i] + self.c[0] * self.r[0] * (self.pBest[i] - self.x[i]) + self.c[1] * self.r[1] * (self.gBest - self.x[i])
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
            print(f"Sebelum: x0 = {self.oldX[0]}, x1 = {self.oldX[1]}, x2 = {self.oldX[2]}")
            print(f"gBest = {self.gBest}")
            print(f"pBest = {self.pBest}")
            print(f"v = {self.v}")
            print(f"Sesudah: x0 = {self.x[0]}, x1 = {self.x[1]}, x2 = {self.x[2]}")
            print(f"Nilai Fungsi: f(x0) = {self.f[0]}, f(x1) = {self.f[1]}, f(x2) = {self.f[2]}")

x = np.random.randint(10, size=5)
sm = SwarmMethod(x, 0, [0.5, 1], [0.5, 0.5], 1)
sm.swarm(3)