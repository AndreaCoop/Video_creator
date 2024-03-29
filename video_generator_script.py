# script to create an animated plot from a simulation

# import data

# import packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# +
# input 

# data from a .txt file
file_data = "sin_expdecay.txt"

#set title and legth of the movie
title_movie = 'example3_20s_5dpi'
length_movie = 20 # in seconds

n_datapoint_per_interval = 5

# Decorate the plot
X_label = 'time [s]'
Y_label = 'Signal'
plot_title = 'Best plot ever!'


# +

def video_generator(file_data, X_label, Y_label, plot_title, movie_title, movie_length, n_datapoint_per_interval=1):
    """Create a video animation from a data set
    
    The video is saved in a .mp4 file in the same folder
    
    Parameters
    ----------
    file_data : .txt file 
                file containing the data to plot, in the format of a np.array([x, y])
    X_label : str
              label of X axis
    Y_label : str
              label of y axis
    plot_title : str
                 title of the plot
    movie_title : str
                  name to give to the .mp4 file when saved
    movie_length : int
                   duration in seconds of the movie
    n_datapoint_per interval: int, optional 
                              number of datapoints taken in each frame (default=1)
                              if n_datapoint_per interval = 1 : it takes as number of frames as the number of datapoints
                              if n_datapoint_per interval > 1 : there will be less frames, 
                                                                the video will be less smooth 
                                                                but it will take less time to create it
    """
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
video_generator(file_data, X_label, Y_label, plot_title, title_movie, length_movie, n_datapoint_per_interval)


