
import numpy as np

def qPointInTriangle(point,triangle):
    '''
    function : if point in the triangle
    point : array([x,y])
    triangle : array([x1,x2,x3],
                     [y1,y2,y3])
    '''

    pointHomo = np.hstack((point, np.array([1])))
    triangleHomo = np.vstack((triangle, np.array([1,1,1])))

    x = np.linalg.solve(triangleHomo, pointHomo)
    if np.min(x) >= 0:
        return True

    return False

def qHaffineMapSolver(srcTri, dstTri):
    
    '''
    haffine map from srcTriangle to dstTriangle
    :param srcTri:array([x1,x2,x3],
                        [y1,y2,y3])
    :param dstTri:array([x1,x2,x3],
                        [y1,y2,y3])
    :return:array[[h1,k1],[h2,k2],[c1,c2]]
    '''

    matrixA = np.vstack((srcTri, np.array([1,1,1]))).transpose()
    matrixAInv = np.linalg.inv(matrixA)

    paraX = np.dot(matrixAInv, dstTri[0])
    paraY = np.dot(matrixAInv, dstTri[1])

    matrix = np.vstack((paraX[:2], paraY[:2])).transpose()
    offset = np.hstack((paraX[2], paraY[2]))

    return np.vstack((matrix, offset))

def qHaffineMapper(point, hafMap):
    '''
    use haffinemap to point
    :param point: array([x,y])
    :param hafMap: (array[[h1,k1],[h2,k2]], array([c1,c2]))
    :return: point, array([x,y])
    '''

    matrix = hafMap[0:2]
    offset = hafMap[2]
    return np.dot(matrix, point) + offset



if __name__ == '__main__':
    #point = np.array([0.5,0.2])
    #triangle = np.array([[0,1,0],[0,1,1]])

    #for i in range(1000):
    #    pointInTriangle(point, triangle)

    srcTriangle = np.array([[0,1,1],[0,0,1]])
    dstTriangle = np.array([[0,2,2],[0,0,2]])

    for i in range(1280):
        qHaffineMapSolver(srcTriangle, dstTriangle)
        qHaffineMapSolver(dstTriangle, srcTriangle)