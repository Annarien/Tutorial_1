import numpy as np

#create methods 
def Integral_Of_Cos(n):
    x = np.linspace(0.0, np.pi/2, n) #n is number of elements to be returned in the vector of n evenly spaced numbers
    y = np.cos(x)

    dx = np.pi/2/n #change in x pi/2 divided by number of evenly spaced elements

    integralOfCos = y.sum()*dx
    return integralOfCos

def Simpsons_Integral_Of_Cos(n):
    x = np.linspace(0.0, np.pi/2, n)
    y = np.cos(x)

    x_even = y[2:-1:2]
    x_odd = y[1:-1:2]

    dx = np.pi/2/n*2 # times 2 is from lecture notes, ask Sievers why

    simpsonIntOfCos = dx*(y[0]/6 + x_even.sum()/3 + x_odd.sum()*2/3 + y[-1]/6)
    return simpsonIntOfCos

range = [10, 30, 100, 300, 1000]
for n in range:
    simpsonsIntegral = Simpsons_Integral_Of_Cos(n)
    print ("The Simpson's integral of cos(x) for " +  str(n) + " element(s) = " + str(simpsonsIntegral))



#Part 2 - accuracy of 10 (his 11 - our 10) points with Simpson's Rule.
#1 - Establish value of Simpon's rule with 10 evenly spaced elements in a vector.
#2 - Starting at 1 element in a vector, calculate the value of the integral of cos(x).
#3 - While the value is not that of the goal (from step 1), we increment our element count by 1 and repeat step 2.
#4 - Repeat step 3 until our value is equal to the goal.
#5 - We know from observation that 10 elements in the vector for the standard integral of cos(x) is > Simpson's rule with 10 elements for cos(x), so break at 10 to avoid infinite loop.

#1 - The goal
goal = Simpsons_Integral_Of_Cos(10)
print ("\nThe goal is: " + str(goal) + "\n")
numberOfElementsNeeded = -1 #so that if its still -1 after the loop, we knw we didnt find the right number of elements

#2 - Start
elementCount = 1

#3 - Begin looping
while (elementCount <= 10):
    valueOfIntegralOfCos = Integral_Of_Cos(elementCount)
    print ("The value of cos(x) for " + str(elementCount) + " element(s) = " + str(valueOfIntegralOfCos))
    if (valueOfIntegralOfCos == goal):
        numberOfElementsNeeded = elementCount
        break

    elementCount = elementCount + 1

# Print out results
if (numberOfElementsNeeded != -1): #not -1 then we found the right number of elements
    print ("\nThe number of elements needed to achieve the same accuracy as Simpson's rule is: " + str(numberOfElementsNeeded))
else:
    print ("\nThere are no numbers between 0 and 10 that achieve the same accuracy as Simpson's rule.")
    print ("We can see that the integral of cos(x) for 10 element is greater than the Simpson's integral of cos(x) for 10 element where n=10.")
    print ("We can see in the data that n must be equal to roughly 3 in the cos integral for us to recieve a similar result in the Simpson's rule.")