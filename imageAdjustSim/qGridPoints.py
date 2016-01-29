import numpy as np
import inverseMapUtil
import math

class qGridPoints:

    def __init__(self, width, height, res):

        self.raw = math.ceil(float(width)/res)
        self.col = math.ceil(float(height)/res)
        self.res = res
        self.grid = np.empty((self.raw, self.col, 1, 4))

        self.refresh()

    def refresh(self):
        for i in range(self.raw):
            for j in range(self.col):
                self.grif[i,j] = [0,0,1,0]#[x,y,outOfBoundary,calcFlag]

    def __updateByTriangle(self, triangle, map):
        #TODO __updateByTriangle
        maxX = max(triangle[0])
        minX = min(triangle[0])
        maxY = max(triangle[1])
        minY = min(triangle[1])

        indexMaxX = math.ceil(float(maxX)/self.res)
        indexMinX = minX/self.res



    def update(self, ctrlPoints):
        #TODO update