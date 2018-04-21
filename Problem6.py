import numpy as np
from matplotlib import pyplot as plt

#methods
def Integral_Of_Cos(n):
    x = np.linspace(0.0, np.pi/2, n)
    y = np.cos(x)

    dx = np.pi/2/n
    return y.sum()*dx

def Simpsons_Integral_Of_Cos(n):
    x = np.linspace(0.0, np.pi/2, n)

    y = np.cos(x)
    x_even = y[2:-1:2]
    x_odd = y[1:-1:2]

    dx = np.pi/2/n*2
    
    return dx*(y[0]/6 + x_even.sum()/3 + x_odd.sum()*2/3 + y[-1]/6)


points = [10, 30, 100, 300, 1000]                                       # points on x-axis between 0 and pi/2
points = np.array(points)                                               # convert object of points to array

simple_errs = np.zeros(points.size)                                     # get array of zeroes equal size of point array - for simple integration of cos(X)
simpson_errs = np.zeros(points.size)                                    # get array of zeroes equal size of point array - for simpson's integration of cos(X)

for index in range(points.size):                                        # iterate through elements in array
    n = points[index]
    simple_errs[index] = np.absolute(Integral_Of_Cos(n) - 1)            # get the error for the simple integral of cos(x) and take absolute value
    simpson_errs[index] = np.absolute(Simpsons_Integral_Of_Cos(n) - 1)  # get the error for the simpson's integral of cos(x) and take absolute value

plt.plot(points, simple_errs)                                           # plot on x axis-points, y-axis simple err
plt.plot(points, simpson_errs)                                          # plot on x axis-points, y-axis simpson's err

ax = plt.gca()                                                          #ASK SEIVERS!!!!!!!!!!!

ax.set_yscale('log')                                                    # graph to be of log form
ax.set_xscale('log')
plt.show()