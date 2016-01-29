#import Image
from qCtrlPoints import qCtrlPoints
import pylab as pl

def drawCtrlPoints(ctrlPoints):
    if isinstance(ctrlPoints, qCtrlPoints):
        pass
    else:
        return

    raw = ctrlPoints.raw
    col = ctrlPoints.col

    x = []
    y = []

    for i in range(raw+2):
        for j in range(col+2):
            x.append(ctrlPoints.dst[i,j,0])
            y.append(ctrlPoints.dst[i,j,1])

    print x
    print y
    pl.plot(x, y, 'r*')
    pl.show()

import math

print math.ceil(0.7)