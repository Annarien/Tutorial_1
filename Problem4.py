
import numpy
#take all odd points in array from 5 to 10 to get 5,7,9
x=numpy.arange(5,10,2)
print (x)

#have an array of y from 0-10
y=numpy.arange(0,10,1)
#taking all point in array-this is called array slicing
odd = y[1:-1:2] #all odd from 0-10
#even = y[0:-1:2] #all even from 0-10
print(odd)
#print(even)

#to print even from 0-10, skipping first even number start at 2, and goes up to last even but not including 10. 
even2 = y[2:-1:2]
print(even2)

