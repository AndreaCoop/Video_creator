# script to create an animated plot from a simulation

# import data

pip install drawnow

# import packages
import numpy as np
import matplotlib as plt
from drawnow import drawnow, figure

# load data
[X,Y] = np.loadtxt("testSin.txt")

# function to generate plot
def draw_fig_real(axes):
    #figure() # don't call, otherwise opens new window
    # plt.pyplot.imshow(z, interpolation='nearest')
    #plt.colorbar()
    #show()
    axes1.plot(X1,Y1)

# video
N = 16
fig, axes1 = plt.pyplot.subplots()
axes1.set_xlim(0,9)
for i in range(1,N):
    j=i*(len(X)//N)
    X1=X[0:j]
    Y1=Y[0:j]
    drawnow(draw_fig_real)


