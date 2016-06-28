'''
from matplotlib import pyplot as plt
import sys

x=[2,4,6]
y=[1,3,5]


plt.legend()
plt.plot()
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")
plt.show()

'''
'''
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)

plt.show()
'''
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')

plt.show()

'''
#This is to create graph
import numpy as np
import matplotlib.pyplot as plt

n = 20
Z = np.random.uniform(0,1,n)
plt.pie(Z)
plt.show()