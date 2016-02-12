import numpy as np
import inverseMapUtil


class qCtrlPoints:

    def __init__(self, width, height, rawNum, colNum):
        self.src = np.empty((rawNum+2, colNum+2, 2))
        self.dst = np.empty((rawNum+2, colNum+2, 2))
        self.raw = rawNum
        self.col = colNum

        self.map = np.empty((self.raw+1,2*(self.col+1),3,2))
        self.srcTriangle = np.empty((self.raw+1, 2*(self.col+1), 2, 3))
        self.dstTriangle = np.empty((self.raw+1, 2*(self.col+1), 2, 3))

        stepRaw = float(width - 1) / float(colNum - 1)
        stepCol = float(height - 1) / float(rawNum - 1)

        for i in range(rawNum):
            for j in range(colNum):
                self.src[i+1, j+1] = [j * stepRaw, i * stepCol]
                self.dst[i+1, j+1] = [j * stepRaw, i * stepCol]

        self.__extendBoundary(self.src)
        self.__extendBoundary(self.dst)

    def __extendBoundary(self, points):

        points[0,0] = 2*points[1,1] - points[2,2]
        points[self.raw+1,self.col+1] = 2*points[self.raw,self.col] - points[self.raw-1,self.col-1]
        points[0,self.col+1] = 2*points[1,self.col] - points[2,self.col-1]
        points[self.raw+1,0] = 2*points[self.raw,1] - points[self.raw-1,2]

        points[0,1:self.col+1] = 2*points[1,1:self.col+1] - points[2,1:self.col+1]
        points[self.raw+1,1:self.col+1] = 2*points[self.raw,1:self.col+1] - points[self.raw-1,1:self.col+1]

        points[1:self.raw+1,0] = 2*points[1:self.raw+1,1] - points[1:self.raw+1,2]
        points[1:self.raw+1,self.col+1] = 2*points[1:self.raw+1,self.col] - points[1:self.raw+1,self.col-1]


    def extendBoundaryDst(self):
        self.__extendBoundary(self.dst)
        self.calcTriangle()
        self.calcMap()

    def setPoint(self, raw, col, x, y):
        self.dst[raw+1, col+1] = [x, y]

    def calcTriangle(self):

        for i in range(self.raw+1):
            for j in range(self.col+1):
                self.srcTriangle[i, 2*j]   = np.transpose([self.src[i,j],self.src[i+1,j+1],self.src[i+1,j]])
                self.srcTriangle[i, 2*j+1] = np.transpose([self.src[i,j],self.src[i,j+1],self.src[i+1,j+1]])
                self.dstTriangle[i, 2*j]   = np.transpose([self.dst[i,j],self.dst[i+1,j+1],self.dst[i+1,j]])
                self.dstTriangle[i, 2*j+1] = np.transpose([self.dst[i,j],self.dst[i,j+1],self.dst[i+1,j+1]])

    def getTriangle(self):
        return (self.srcTriangle, self.dstTriangle)

    def getSrcTriangle(self):
        return self.srcTriangle

    def getDstTriangle(self):
        return self.dstTriangle

    def calcMap(self):

        for i in range(self.raw+1):
            for j in range(2*(self.col+1)):
                self.map[i,j] = inverseMapUtil.qHaffineMapSolver(self.dstTriangle[i,j], self.srcTriangle[i,j])

    def getMap(self):
        return self.map

if __name__ == '__main__':

    ctrlPointsA = qCtrlPoints(1024, 768, 20, 20)

    print ctrlPointsA.src
    print ctrlPointsA.dst

    ctrlPointsA.setPoint(0,0,-20,0)
    ctrlPointsA.extendBoundaryDst()
    triangleSrc = ctrlPointsA.getTriangle()[0]
    triangleDst = ctrlPointsA.getTriangle()[1]
    print triangleSrc[0, 0]
    print triangleDst[0, 0]
    print ctrlPointsA.getMap()[0,0]

