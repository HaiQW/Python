import numpy as np
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D

N = 1000
T1 = np.random.rand(N)
T2 = np.random.rand(N)
T3 = np.random.rand(N)
Z1 = np.random.rand(N)
w = np.sqrt(2)
r = np.sqrt( -2 * np.log(T1*1/w))
theta1 = 2 * np.pi * T2
theta2 =  2 * np.pi * T3
X1 = r * np.sin(theta1) * np.cos(theta2)
Y1 = r * np.sin(theta1) * np.sin(theta2)
Z1 = r * np.cos(theta1)

N = 5
T3 = np.random.rand(N)
T4 = np.random.rand(N)
T5 = np.random.rand(N)
w = np.sqrt(2)
r = np.sqrt( -2 *(0.01) * np.log(T3*1/w))
theta1 = 2 * np.pi * T4
theta2 =  2 * np.pi * T5
X2 = r * np.sin(theta1) * np.cos(theta2) + 4
Y2 = r * np.sin(theta1) * np.sin(theta2) + 4
Z2 = r * np.cos(theta1) + 1
#heatmap2, xedges2, yedges2 = np.histogram2d(X1,Y1,bins = 200)
#extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
#extent2 = [xedges2[0], xedges2[-1], yedges2[0], yedges2[-1]]



fig = plot.figure()
ax = fig.add_subplot(111,projection = '3d')
ax.scatter(X1,Y1,Z1,color = 'g')
ax.scatter(X2,Y2,Z2,color = 'r')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
g_circle = plot.Circle(0,1, fc="g")
r_circle = plot.Circle(0,1, fc="r")
ax.legend([g_circle,r_circle],['major','anomaly'])
#print heatmap

#plot.imshow(heatmap,extent = extent)

#plot.imshow(heatmap2,cmap = plot.cm.Reds_r,extent = extent2)

plot.show()
