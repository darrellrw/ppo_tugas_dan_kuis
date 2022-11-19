import numpy as np
import sympy as sp

tab = []

def z():
    return [8, 6]

def slack():
    return [[4, 2], [2, 4]]

def b():
    return [60, 48]

def tableuFirst():
    if(len(tab) == 0):
        tab0 = []
        tab0.append(1)
        for j in range(len(z())):
            tab0.append(-1 * z()[j])
        for k in range(len(z())):
            tab0.append(0)
        tab0.append(0)
        tab.append(tab0)
        # tab.append([1, -1 * z()[0], -1 * z()[1], 0, 0, 0])
        for i in range(len(slack())):
            tabx = []
            # tab.append([0, slack()[i][0], slack()[i][1], 0, 0, b()[i]])
            tabx.append(0)
            for f in range(len(z())):
                tabx.append(slack()[i][f])
            for h in range(len(z())):
                tabx.append(0)
            tabx.append(b()[i])
            tab.append(tabx)
            tab[i + 1][len(z())+ 1 + i] = 1

def coloumnKey():
    xTab = []
    for i in range(len(z())):
        xTab.append(tab[0][i + 1])
    return tab[0].index(min(xTab))

def rowKey():
    cTab = []
    for i in range(len(slack())):
        ratio = tab[i + 1][len(tab[0]) - 1] / tab[i + 1][coloumnKey()]
        cTab.append(ratio)
    return cTab.index(min(cTab)) + 1

tableuFirst()
print(tab)