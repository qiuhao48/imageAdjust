#import Image
from qCtrlPoints import qCtrlPoints
import inverseMapUtil
import qGridPoints
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

ctrlPntsA = qCtrlPoints(1024, 768, 2, 2)
GridPntsA = qGridPoints.qGridPoints(1024, 768, 32)

drawCtrlPoints(ctrlPntsA)

GridPntsA.update(ctrlPntsA)

print GridPntsA.grid

