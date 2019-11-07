# script to create an animated plot from a simulation

# import data

pip install drawnow

# import packages
import numpy as np
import matplotlib.pyplot as plt
from drawnow import drawnow, figure

# load data
[X,Y] = np.loadtxt("testSin.txt")

# function to generate plot at each frame
def draw_fig_real():
    #figure() # don't call, otherwise opens new window
    # plt.pyplot.imshow(z, interpolation='nearest')
    #plt.colorbar()
    #show()
    plt.ion()
    fig, axes1 = plt.subplots()
    axes1.set_xlim(0,9)
    axes1.plot(X1,Y1)

# for loop to create many frames
N = 16 # number of frames
for i in range(1,N):
    j=i*(len(X)//N)
    X1=X[0:j]
    Y1=Y[0:j]
    draw_fig_real()


