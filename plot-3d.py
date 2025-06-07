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
    [0, 1, 2], [0, 2, 3],  # x平面
    [4, 5, 6], [4, 6, 7],  # y平面
    [8, 9, 10], [8, 10, 11],  # z平面
])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = vertices[:, 0]
y = vertices[:, 1]
z = vertices[:, 2]

ax.plot_trisurf(x, y, z, triangles=faces, cmap='viridis', alpha=0.5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Cube Centered at Origin')

# 绘制顶点编号
for i, (xi, yi, zi) in enumerate(vertices):
    ax.text(xi, yi, zi, f'{i+1}', color='red', fontsize=12)

plt.show()

