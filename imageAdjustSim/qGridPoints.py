import numpy as np
import inverseMapUtil
import qCtrlPoints
import math

class qGridPoints:

    def __init__(self, width, height, res):

        self.raw = int(math.ceil(float(width)/res)) # grid raw number
        self.col = int(math.ceil(float(height)/res)) # grid column number
        self.res = res
        self.grid = np.empty((self.raw, self.col, 1, 3)) # empty grid

        self.refresh() # initial grid

    def refresh(self):
        for i in range(self.raw):
            for j in range(self.col):
                self.grid[i,j] = [0,0,0]#[x,y,calcFlag], if calcFlag equals 0, it means that this point is not in  any triangles

    def __updateByTriangle(self, triangle, map):

        maxX = max(triangle[0])
        minX = min(triangle[0])
        maxY = max(triangle[1])
        minY = min(triangle[1])

        indexMaxX = int(math.ceil(float(maxX)/self.res))
        indexMinX = minX/self.res
        indexMaxY = int(math.ceil(float(maxY)/self.res))
        indexMinY = minY/self.res

        if (indexMaxX < 0) or (indexMaxY < 0) or (indexMinX > self.col) or (indexMinY < self.raw):
            return

        if indexMinX < 0:
            indexMinX = 0

        if indexMinY < 0:
            indexMinY = 0

        if indexMaxX > (self.raw-1):
            indexMaxX = self.raw-1

        if indexMaxY > (self.col-1):
            indexMaxY = self.col-1

        for rawIndex in range(indexMinY, indexMaxY+1):
            for colIndex in range(indexMinX, indexMaxX+1):
                # check if point in triangle
                point = np.array([colIndex*self.res, rawIndex*self.res])
                flagTemp = inverseMapUtil.qPointInTriangle(point, triangle)
                if flagTemp:
                    pointMapped = inverseMapUtil.qHaffineMapper(point, map)
                    self.grid[rawIndex, colIndex] = [pointMapped[0],pointMapped[1],1]

    def update(self, ctrlPoints):

        if isinstance(ctrlPoints, qCtrlPoints.qCtrlPoints):
            pass
        else:
            return


        for indexRaw in range(ctrlPoints.raw+1):
            for indexCol in range(2*ctrlPoints.col+2):
                self.__updateByTriangle(ctrlPoints.getDstTriangle()[indexRaw,indexCol], ctrlPoints.getMap()[indexRaw,indexCol])

