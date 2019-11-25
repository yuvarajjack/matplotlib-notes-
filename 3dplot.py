from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

height = np.array([164,175,188,145,163,174,163,195,132,157])
weight = np.array([67,64,53,86,76,43,72,78,56,61])
'''
plt.xlim(130,200)
plt.ylim(40,90)
#to scatter
plt.scatter(height,weight)
plt.title("3D View Scatter")
plt.xlabel("height")
plt.ylabel("weight")
plt.show()
'''

#in 3D
ax = plt.axes(projection = '3d')
ax.scatter3D(height,weight)
ax.set_xlabel("Height")
ax.set_ylabel("Weight")
plt.show()


#plot3D

ax = plt.axes(projection = '3d')
ax.plot3D(height,weight)
ax.set_xlabel("H")
ax.set_label("W")
plt.show()
