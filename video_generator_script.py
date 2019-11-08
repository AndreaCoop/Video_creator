# script to create an animated plot from a simulation

# import data

# pip install drawnow

# pip install opencv-python

# import packages
import numpy as np
import matplotlib.pyplot as plt
#from drawnow import drawnow, figure
#from cv2 import VideoWriter
from matplotlib import animation

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

# +
# code with animation function of matplotlib

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 9), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    line.set_data(X[0:i], Y[0:i])
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1000, interval=2, blit=True)


# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
anim.save('basic_animation.mp4', fps=60, extra_args=['-vcodec', 'libx264'])

plt.show()

# -
help(FuncAnimation)




