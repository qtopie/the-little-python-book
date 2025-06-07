import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

phi = (1+math.sqrt(5))/2

# 以x,y,z和顺时针的顺序编号顶点和边

# 以原点为中心，边长为1的立方体顶点
vertices = np.array([
    [phi, 0, 1],
    [phi, 0, -1],
    [-phi, 0, -1],
    [-phi, 0, 1],

    [1, phi, 0],
    [1, -phi, 0],
    [-1, -phi, 0],
    [-1, phi, 0],

    [0, 1, phi],
    [0, 1, -phi],
    [0, -1, -phi],
    [0, -1, phi],
])

# 立方体的三角面
faces = np.array([
    [0, 8, 11],
    [1, 9, 10],
    [2, 9, 10],
    [3, 8, 11],

    [4, 0, 1],
    [5, 0, 1],
    [6, 2, 3],
    [7, 2, 3],

    [8, 4, 7],
    [9, 4, 7],
    [10, 5, 6],
    [11, 5, 6],

    [0,4,8],
    [1,4,9],
    [1,5,10],
    [0,5,11],

    [3,6,11],
    [2,6,10],
    [2,7,9],
    [3,7,8]
])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = vertices[:, 0]
y = vertices[:, 1]
z = vertices[:, 2]

ax.plot_trisurf(x, y, z, triangles=faces, cmap='viridis', alpha=1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Cube Centered at Origin')

# 绘制顶点编号
for i, (xi, yi, zi) in enumerate(vertices):
    ax.text(xi, yi, zi, f'{i}', color='red', fontsize=12)

plt.show()

