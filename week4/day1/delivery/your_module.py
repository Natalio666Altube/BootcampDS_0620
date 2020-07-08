# This file represents your module.
# Write the code...
import numpy as np 

def mean_visualization():
    """ Draw the mean in a plot """
    return None

def revert(x):
    return x[::-1]


def tamano(array):
    if (array.size == 0):
        print("The given Array is empty")
    else:
        print("The array = ", array) 
 

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
np.concatenate([x, y])

def array1(x,y):
    return np.concatenate([x,y])

f = np.array([1, 2, 3])
z = np.array([3, 2, 1])
g = array1(x=f, y=z)
print(g)



