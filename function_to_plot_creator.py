# Generate the array with the results to plot for creating the video

# # ODE solver
# If your funciton to solve is an ordinary differential equation

# +
import numpy as np
import scipy.integrate as integrate
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def ordinary_differential_equation(x, t, a):
    """Define your ODE
    d(theta)/dt = theta_dot 
    d(theta_dot)/dt = xxx
    
    Parameters
    ----------
    x : length 2 list
        initial conditions:
         x[0] = initial coordinate
         x[1] = initial velocity
    t : vector
        array with time steps 
    a: float
       coefficient
    
    Returns
    -------
    dx/dt : length 2 list
            dxdt[0] = theta_dot
            dxdt[0] = -a*np.sin(theta)
    """
    
    theta, theta_dot = x
    dxdt = [theta_dot, -a*np.sin(theta)]
    return dxdt

# coefficients
a = 1 

# initial conditions:
x0 = [0.5*np.pi, 0.0]

# time vector:

t = np.linspace(0, 20, 101)

sol = odeint(ordinary_differential_equation, x0, t, args=(a,))

results = np.array([t, sol[:, 0]])

np.savetxt("data_diff_eq", results)
# -

# # Plot 
# Only to check visually the results

plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'r', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.show()


# # Sin function Exponential decay 
#
# The following script generate a sin function which exponentially decays after 4 seconds. It saves the result in a txt file and plot the result

# +
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib widget

def exp_sin(x,alpha,x_delay,points):
    """Create an exponential decaying sin function
    
    Parameters
    ----------
    x : np.array
        x values
    alpha : float
            exp(alpha*x)
    x_delay : float
              delay time after which the sin starts decaying
    points : int
             total number of points of X
    Returns
    -------
    z = np.array
    """

    y = np.sin(10*x)
    h = np.exp(-alpha*x)
    z = np.zeros((1000,))
    x_interval = (x[-1]-x[0])/1000
    points_delay = int(x_delay/x_interval)-1
    print(points_delay)
    print(points)
    z[0:points_delay] = y[0:points_delay]
    z[points_delay+1:points] = y[points_delay+1:points]*h[0:800]

    np.savetxt("sin_expdecay.txt",[x, z])

    [X,Z] = np.loadtxt("sin_expdecay.txt")
    fig, axes = plt.subplots()

    axes.plot(X,Z)

x = np.linspace(0,20,1000)
exp_sin(x,0.4,4,1000)
# -

