import numpy as np

def func(x, y):
    return (x + 2*y -7)**2 + (2*x + y - 5)**2

class SwarmMethod:
    def __init__(self, x, y, v, c, r, w):
        self.x = x
        self.y = y
        self.vX = [v, v, v]
        self.vY = [v, v, v]
        self.c = c
        self.r = r
        self.w = w
        self.f = [None, None, None]
        self.gBestX = None
        self.gBestY = None
        self.pBestY = [None, None, None]
        self.pBestX = [None, None, None]
        self.oldX = [None, None, None]
        self.oldY = [None, None, None]
        self.vectorX = [None, None, None]
        self.vectorV = [None, None, None]
        self.vectorGBest = [None, None, None]
        self.vectorPBest = [None, None, None]
    
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

        for i in range(0, n):
            particle(self.x, self.y, self.vX, self.vY)

sm = SwarmMethod([0, 1, -1], [0, 1, -1], 0, [1, 0.5], [1, 1], 1)
sm.swarm(3)