
# Tuple example
# You cannot change values in a tuple:
thistuple = ("apple", "banana", "cherry")
thistuple[1] = "blackcurrant"
# The values will remain the same:
print(thistuple)

##################################################################
# List example
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
# Change the second item:
print(thislist)


##################################################################
import numpy

#print numpy.zeros((1,2))                    #Default type is float
#Output : [[ 0.  0.]] 

#print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int

# tuple use example
nums = tuple(map(int, input().split()))
print (numpy.zeros(nums, dtype = numpy.int))
print (numpy.ones(nums, dtype = numpy.int))


##################################################################

"""
x = 1
y = 2.8
z = 1j
"""
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
