import numpy as np

def func(x):
    return (4 * np.log(x)) - x

def derivFunc(x):
    return (4/x) - 1

def secondDerivFunc(x):
    return -4/(x**2)

class SwarmMethod:
    def __init__(self, x, v, c, r, w):
        self.x = x
        self.v = v
        for i in range(1,len(x)):
            self.v.append(v[0])
        self.c = c
        self.r = r
        self.w = w
        self.f = [None, None, None]
        self.gBest = None
        self.pBest = [None, None, None]

        self.oldX = [None, None, None]
    
    def swarm(self, n):
        def particle(x, v):
            for i in range(len(x)):
                self.x[i] = x[i]
            for i in range(len(v)):
                self.v[i] = v[i]
        def mencariNilaiFungsi(): 
            for i in range(len(self.f)):
                self.f[i] = func(self.x[i])
        def gBest():
            self.gBest = self.x[self.f.index(max(self.f))]
        def pBest():
            if(self.pBest[0] == None):
                for i in range(len(self.x)):
                    self.pBest[i] = self.x[i]
            else:
                for i in range(len(self.x)):
                    if(func(self.oldX[i]) <= self.f[i]):
                        self.pBest[i] = self.x[i]
                    else:
                        self.pBest[i] = self.oldX[i]
        def updateV():
            for i in range(len(self.v)):
                self.v[i] = self.w * self.v[i] + self.c[0] * self.r[0] * (self.pBest[i] - self.x[i]) + self.c[1] * self.r[1] * (self.gBest - self.x[i])
        def updateX():
            for i in range(len(self.x)):
                self.oldX[i] = self.x[i]
                self.x[i] = self.x[i] + self.v[i]

        for i in range(0, n):
            particle(self.x, self.v)
            mencariNilaiFungsi()
            gBest()
            pBest()
            updateV()
            updateX()
            # print(self.oldX, self.x)
            print(f"Iterasi-{i + 1} x1 = {self.x[0]}, x2 = {self.x[1]}, x3 = {self.x[2]}")

sm = SwarmMethod([1,2,6], [0], [0.5, 1], [1,1], 1)
sm.swarm(100)