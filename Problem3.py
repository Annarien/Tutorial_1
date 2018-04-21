import numpy
import math

pi = numpy.pi
#print (pi)
start = 0.0
end = pi/2

# Part 1
# using linspace to make a vector of n evenly spaced numbers between 0 and pi/2
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html
evenlySpacedNumbers=numpy.linspace(start, end)
print (str(evenlySpacedNumbers) + "\n") # \n for new line
rangearray=[10, 30, 100, 300, 1000]
for n in rangearray:
    x = numpy.linspace(start, end, n)
    #print (x)
    y = numpy.cos(x)

    dx = numpy.pi/2/n
    tot=y.sum()*dx
    print("The integral of cos x between " + str(start) + " and "+ str(end) + " is " + str(tot) + " for " + str(n)+" points.")

print("alpha is roughly equal to 1/(number of points in range), where n is the range")
print ("end")

