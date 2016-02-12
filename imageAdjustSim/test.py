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

    xDst = []
    yDst = []
    xSrc = []
    ySrc = []

    for i in range(raw+2):
        for j in range(col+2):
            xDst.append(ctrlPoints.dst[i,j,0])
            yDst.append(ctrlPoints.dst[i,j,1])
            xSrc.append(ctrlPoints.src[i,j,0])
            ySrc.append(ctrlPoints.src[i,j,1])
    #print x
    #print y
    pl.plot(xSrc, ySrc, 'b*')
    pl.plot(xDst, yDst, 'ro')
    pl.show()

def drawGridPoints(gridPoints):
    if isinstance(gridPoints, qGridPoints.qGridPoints):
        pass
    else:
        return

    raw = gridPoints.raw
    col = gridPoints.col

    x = []
    y = []

    for i in range(raw):
        for j in range(col):
            x.append(gridPoints.grid[i,j,0])
            y.append(gridPoints.grid[i,j,1])

    #print x
    #print y
    pl.plot(x, y, 'r*')
    pl.show()



ctrlPntsA = qCtrlPoints(1920, 1080, 4, 4)

ctrlPntsA.setPoint(0,0,20,20)
ctrlPntsA.setPoint(3,3,1900,1000)
ctrlPntsA.setPoint(0,3,1900,20)
ctrlPntsA.setPoint(3,0,20,1000)
ctrlPntsA.extendBoundaryDst()
#drawCtrlPoints(ctrlPntsA)

GridPntsA = qGridPoints.qGridPoints(1920, 1080, 32)
GridPntsA.update(ctrlPntsA)

#print GridPntsA.grid
drawGridPoints(GridPntsA)
