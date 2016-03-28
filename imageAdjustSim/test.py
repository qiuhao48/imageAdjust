#import Image
from qCtrlPoints import qCtrlPoints
import inverseMapUtil
import qGridPoints
import pylab as pl
import numpy as np

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

width = 2000
height = 2000
row = 20
col = 20
k = 15
res = 32

pts00 = np.array([500,20])
pts01 = np.array([1500,30])
pts10 = np.array([100,1899])
pts11 = np.array([1899,1799])


ctrlPntsA = qCtrlPoints(width, height, row, col, k)

for i in range(row):
    for j in range(col):
        temp1 = pts00*(col-1-j)/(col-1)+pts01*j/(col-1)
        temp2 = pts10*(col-1-j)/(col-1)+pts11*j/(col-1)
        temp  = temp1*(row-1-i)/(row-1)+temp2*i/(row-1)
        ctrlPntsA.setPoint(i,j,temp[0],temp[1])

ctrlPntsA.extendBoundaryDst()
drawCtrlPoints(ctrlPntsA)

GridPntsA = qGridPoints.qGridPoints(width, height, res)
GridPntsA.update(ctrlPntsA)

#print GridPntsA.grid
drawGridPoints(GridPntsA)



# src grid
file = open('C:/Users/qiule/Desktop/src.dat','w')

str_temp = 'width = %d\nheight = %d\nrow = %d\ncol = %d\nk = %d\nres = %d\n\n' % (width, height, row, col, k, res)
file.write(str_temp)

str_temp = '[src grid] %d * %d\n\n' % (row+2, col+2)
file.write(str_temp)
for i in range(row+2):
    for j in range(col+2):
        str_temp = '%f %f\n' % (ctrlPntsA.src[i,j,0],ctrlPntsA.src[i,j,1])
        file.write(str_temp)
file.write('\n\n')
#file.close()

#dst grid
#file = open('C:/Users/qiule/Desktop/dst.dat','w')
str_temp = '[dst grid] %d * %d\n\n' % (row+2, col+2)
file.write(str_temp)
for i in range(row+2):
    for j in range(col+2):
        str_temp = '%f %f\n' % (ctrlPntsA.dst[i,j,0],ctrlPntsA.dst[i,j,1])
        file.write(str_temp)
file.write('\n\n')
#file.close()

#lut
str_temp = '[lut] %d * %d\n\n' % (GridPntsA.raw, GridPntsA.col)
file.write(str_temp)
for i in range(GridPntsA.raw):
    for j in range(GridPntsA.col):
        str_temp = '%f %f\n' % (GridPntsA.grid[i,j,0],GridPntsA.grid[i,j,1])
        file.write(str_temp)

file.close()

for i in range(GridPntsA.raw):
    for j in range(GridPntsA.col):
        if GridPntsA.grid[i,j,2]==0:
            print i,j

