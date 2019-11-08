# script to create an animated plot from a simulation

# import data

# import packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# +
# input esterni - cancella

# data from a .txt file
file_data = "sin_expdecay.txt"

#set title and legth of the movie
title_movie = 'prova2'
length_movie = 5 # in seconds

n_datapoint_per_interval = 1

# Decorate the plot
X_label = 'x'
Y_label = 'sin(x)'
plot_title = 'Best plot ever!'


# +

def video_generator(file_data, n_datapoint_per_interval, X_label, Y_label, plot_title, movie_title, movie_length):

    # load data
    [X,Y] = np.loadtxt(file_data)

    # set number of frames for creating the plot
    X_length = len(X)
    X_interval = X_length // n_datapoint_per_interval

    # set limits of the plot
    X_start = X[0]
    X_stop = X[-1]
    Y_gap = (np.amax(Y) - np.amin(Y)) * 0.1
    Y_start = np.amin(Y) - Y_gap
    Y_stop = np.amax(Y) + Y_gap


    # print(X_length, n_datapoint_per_interval, X_interval)

    # code with animation function of matplotlib

    # First set up the figure, the axis, and the plot element we want to animate
    fig = plt.figure()
    ax = plt.axes(xlim=(X_start, X_stop), ylim=(Y_start, Y_stop))
    ax.set_xlabel(X_label)
    ax.set_ylabel(Y_label)
    ax.set_title(plot_title)
    line, = ax.plot([], [], lw=2)

    # set movie_title
    title_movie = movie_title + '.mp4'

    # frames per second
    frames_per_seconds = (X_interval+1) // movie_length  

    # initialization function: plot the background of each frame
    def init():
        line.set_data([], [])
        return line,

    # animation function.  This is called sequentially
    def animate(i):
        line.set_data(X[0:i*n_datapoint_per_interval], Y[0:i*n_datapoint_per_interval])
        return line,

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=X_interval+1, interval=200, blit=True)


    # save the animation as an mp4.  This requires ffmpeg or mencoder to be
    # installed.  The extra_args ensure that the x264 codec is used, so that
    # the video can be embedded in html5.  You may need to adjust this for
    # your system: for more information, see
    # http://matplotlib.sourceforge.net/api/animation_api.html
    anim.save(title_movie, fps=frames_per_seconds, extra_args=['-vcodec', 'libx264'])
    # fps: frames per second in the movie 
    #      --> the higher the number of fps, the faster will be animation in the movie
    #       es. if frames = 1000 in FuncAnimation and fps = 100: the movie will last 10 seconds

    plt.show()
# -
video_generator(file_data, n_datapoint_per_interval, X_label, Y_label, plot_title, title_movie, length_movie)


