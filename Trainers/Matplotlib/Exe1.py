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

# git checkout master
# git push origin +HEAD

# This is to create graph
'''
import numpy as np
import matplotlib.pyplot as plt

n = 20
Z = np.random.uniform(0,1,n)
plt.pie(Z)
plt.show()
'''
import time
import re
from bs4 import BeautifulSoup


pages = re.compile('button pagenum">.*?</span>')
#pglist = ['button pagenum">no results</span>', 'button pagenum">no results</span>']
#pg = pglist.pop(0)

var = "<div><span class=\"button pagenum\"><span class=\"range\"><span class=\"rangeFrom\">1</span> to <span class=\"rangeTo\">100</span></span> of <span class=\"totalcount\">159</span></span></div>"

soup = BeautifulSoup(var)
print soup

'''
list = pages.findall(var)
print list
time.sleep(100)
'''

'''
print findall(var)
print pg
print pg.find('no')
print pg.find('results')
print pg.find('of')

time.sleep(100)

if pg.find('of') == -1:
    print pg.findall('no')
    print pg.findall('results')
    print "Results MINUS ONE"
elif pg.find('no') == 1:
    print "Results ONE"
elif pg.find('no') == 0:
    print "Results ZERO"
else:
    print "printing nothing"
'''