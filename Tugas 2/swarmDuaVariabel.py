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

class SwarmMethod:
    def __init__(self, x, y, vX, vY, c, r, w):
        self.x = x
        self.y = y

        self.vX = vX
        self.vY = vY
        for i in range(1,len(x)):
            self.vX.append(vX[0])
            self.vY.append(vY[0])

        self.c = c
        self.r = r
        self.w = w

        self.f = [None, None, None, None]

        self.gBestX = None
        self.gBestY = None

        self.pBestY = [None, None, None, None]
        self.pBestX = [None, None, None, None]

        self.oldX = [None, None, None, None]
        self.oldY = [None, None, None, None]

        self.vectorX = [None, None, None, None]
        self.vectorV = [None, None, None, None]
        self.vectorGBest = [None, None, None, None]
        self.vectorPBest = [None, None, None, None]
    
    def swarm(self, n):
        def particle(x, y, vX, vY):
            for i in range(len(x)):
                self.x[i] = x[i]
                self.y[i] = y[i]
                self.vectorX[i] = np.matrix([[x[i]], [y[i]]])
            for i in range(len(vX)):
                self.vX[i] = vX[i]
                self.vY[i] = vY[i]
                self.vectorV[i] = np.matrix([[vX[i]], [vY[i]]])

        def mencariNilaiFungsi(): 
            for i in range(len(self.f)):
                self.f[i] = func(self.x[i], self.y[i])

        def gBest():
            self.gBestX = self.x[self.f.index(max(self.f))]
            self.gBestY = self.x[self.f.index(max(self.f))]
            self.vectorGBest = np.matrix([[self.gBestX], [self.gBestY]])

        def pBest():
            if(self.pBestX[0] == None):
                for i in range(len(self.x)):
                    self.pBestX[i] = self.x[i]
                    self.pBestY[i] = self.y[i]
                    self.vectorPBest = np.matrix([[self.pBestX[i]], [self.pBestY[i]]])
            else:
                for i in range(len(self.x)):
                    if(func(self.oldX[i], self.oldY[i]) <= self.f[i]):
                        self.pBestX[i] = self.x[i]
                    else:
                        self.pBestX[i] = self.oldX[i]
                    
                    if(func(self.oldX[i], self.oldY[i]) <= self.f[i]):
                        self.pBestY[i] = self.y[i]
                    else:
                        self.pBestY[i] = self.oldY[i]
                    self.vectorPBest = np.matrix([[self.pBestX[i]], [self.pBestY[i]]])

        def updateV():
            for i in range(len(self.vX)):
                self.vectorV[i] = self.w * self.vectorV[i] + self.c[0] * self.r[0] * (self.vectorV[i] - self.vectorX[i]) + self.c[1] * self.r[1] * (self.vectorGBest - self.vectorX[i])
                self.vX[i] = self.vectorV[i][0, 0]
                self.vY[i] = self.vectorV[i][1, 0]

        def updateX():
            for i in range(len(self.x)):
                self.oldX[i] = self.x[i]
                self.oldY[i] = self.y[i]
                self.vectorX[i] = self.vectorX[i] + self.vectorV[i]

                self.x[i] = self.vectorX[i][0, 0]
                self.y[i] = self.vectorX[i][1, 0]

        print(f"Iterasi-0 x1 = {self.x[0], self.y[0]}, x2 = {self.x[1], self.y[1]}, x3 = {self.x[2], self.y[2]}, x4 = {self.x[3], self.y[3]}")
        for i in range(0, n):
            particle(self.x, self.y, self.vX, self.vY)
            mencariNilaiFungsi()
            gBest()
            pBest()
            updateV()
            updateX()
            print(f"Iterasi-{i + 1} x1 = {self.vectorX[0][0, 0], self.vectorX[0][1, 0]}, x2 = {self.vectorX[1][0, 0], self.vectorX[1][1, 0]}, x3 = {self.vectorX[2][0, 0], self.vectorX[2][1, 0]}, x4 = {self.vectorX[3][0, 0], self.vectorX[3][1, 0]}")

sm = SwarmMethod([1, 3, -2, 5], [-1, 0, 2, 5], [0], [0], [1, 0.5], [1, 1], 1)
sm.swarm(3)