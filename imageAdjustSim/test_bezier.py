import bezier_grid_2D
import pylab as pl


def draw_mesh(ctrl_points, mesh):
    if isinstance(ctrl_points, bezier_grid_2D.CtrlPoint):
        pass
    else:
        return

    if isinstance(mesh, bezier_grid_2D.Mesh2D):
        pass
    else:
        return

    raw = ctrl_points.raw
    col = ctrl_points.col

    x_ctrl_p = []
    y_ctrl_p = []

    for i in range(raw):
        for j in range(col):
            x_ctrl_p.append(ctrl_points.gridX[i, j])
            y_ctrl_p.append(ctrl_points.gridY[i, j])

    raw = mesh.raw
    col = mesh.col

    x_mesh = []
    y_mesh = []

    for i in range(raw):
        for j in range(col):
            x_mesh.append(mesh.mesh[i, j, 0])
            y_mesh.append(mesh.mesh[i, j, 1])

    pl.plot(x_mesh, y_mesh, 'go')
    pl.plot(x_ctrl_p, y_ctrl_p, 'ro')
    pl.show()

ctrl_point = bezier_grid_2D.CtrlPoint(1920, 1080, 4, 8)

ctrl_point.set_point(1, 1, 480, 200)
ctrl_point.set_point(0, 1, 500, -200)
ctrl_point.set_point(0, 2, 1000, -200)
ctrl_point.set_point(0, 3, 1500, -200)

mesh = bezier_grid_2D.Mesh2D(20, 40)
mesh.update_by_ctrl_point(ctrl_point)

draw_mesh(ctrl_point, mesh)
