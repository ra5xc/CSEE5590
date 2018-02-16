import numpy as np #import the numpy library
from collections import Counter
from datetime import datetime
import datetime
import time

a = time.time()
def random_array():
    z= np.random.randint(0, 20,15) #creating random values
    print(z)
    return z
def most_frequent_value(z):
    most_frequency=np.bincount(z).argmax() #this would give the most frequent value
                                    #however if 2 values are most frequent, it wont display both of the values
    unique_values=np.unique(z) #this would create array of uniques values
    print("The most frequent values have been repeated %d times and the values are "%(z.count(most_frequency)))
    for i in unique_values:
        if z.count(most_frequency)==z.count(i):
            print(i)




z=random_array()

#z= [ 6 , 4 , 9 , 3,  9 ,18,  7, 15,  9, 17,  1 ,19, 11, 17,  0]
most_frequent_value(list(z))

b = time.time()
print("Time to simulate ",(b-a))




