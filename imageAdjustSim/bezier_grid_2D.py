import numpy as np
import math
import operator


class SurfacePoint:
    def __init__(self):
        pass


class CtrlPoint:

    def __init__(self, width, height, raw, col):
        self.raw = raw
        self.col = col
        self.width = width
        self.height = height
        self.gridX = np.empty([self.raw, self.col])
        self.gridY = np.empty([self.raw, self.col])

        self.refresh()

    def refresh(self):
        step_x = (self.width-1.0)/(self.col-1)
        step_y = (self.height-1.0)/(self.raw-1)

        for i in range(self.raw):
            for j in range(self.col):
                self.gridX[i, j] = step_x*j
                self.gridY[i, j] = step_y*i

    def set_point(self, raw, col, x, y):
        self.gridX[raw, col] = x
        self.gridY[raw, col] = y

    def bezier_mesh_2d(self, u, v):

        u_vector = CtrlPoint.__bezier_base_vector(u, self.col-1)
        v_vector = CtrlPoint.__bezier_base_vector(v, self.raw-1)

        u_x = np.dot(self.gridX, u_vector)
        u_y = np.dot(self.gridY, u_vector)

        v_x = np.dot(u_x, v_vector)
        v_y = np.dot(u_y, v_vector)

        return np.array([v_x, v_y])

    @staticmethod
    def __bezier_base_vector(t, n):
        vector = [CtrlPoint.__comb_number(n, i)*math.pow(1-t, n-i)*math.pow(t, i) for i in range(n+1)]
        return np.array(vector)

    @staticmethod
    def __comb_number(n, k):
        if k == 0:
            return 1
        else:
            return reduce(operator.mul, range(n - k + 1, n + 1)) / reduce(operator.mul, range(1, k + 1))


class Mesh2D:

    def __init__(self, raw, col):
        self.raw = raw
        self.col = col
        self.mesh = np.empty([raw, col, 2])

    def update_by_ctrl_point(self, ctrl_point):

        if isinstance(ctrl_point, CtrlPoint):
            pass
        else:
            return

        step_x = 1.0/(self.col-1)
        step_y = 1.0/(self.raw-1)

        for i in range(self.raw):
            for j in range(self.col):
                self.mesh[i, j] = ctrl_point.bezier_mesh_2d(step_x*j, step_y*i)

    def set_point(self, raw, col, x, y):
        self.mesh[raw, col] = [x, y]

