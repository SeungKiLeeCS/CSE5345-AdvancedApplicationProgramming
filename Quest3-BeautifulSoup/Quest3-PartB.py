from collections import Counter
from functools import reduce
import matplotlib.pyplot as plt
import numpy as np
import random

# Utility function
def runtime(f):
    import timeit
    start = timeit.default_timer()
    f
    end = timeit.default_timer()
    return(end - start) 

# My Function
def wordsInStringToDictWordCount(istr):
    
    return_dict = {}
    
    if len(istr) > 1:      
        temp_list = istr.split()
        
        for i in temp_list:
            if i in return_dict:
                return_dict[i] += 1
            else:
                return_dict[i] = 1
                
    return return_dict

# Counter class
def beatTheCounter(istr):
    cnt = Counter()
    temp_list = istr.split()
    
    for i in temp_list:
        cnt[i] += 1

    return cnt

with open('./lstring.txt', 'r') as fstr:
    longstring = fstr.read().replace('\n', ' ')

mytime = runtime(wordsInStringToDictWordCount(longstring))
cnttime = runtime(beatTheCounter(longstring))

# Run the function 100 times and average the result
mytimelist = []
cnttimelist = []

for i in range (0,100):
    mytimelist.append(runtime(wordsInStringToDictWordCount(longstring)))
    cnttimelist.append(runtime(beatTheCounter(longstring)))

avg_mytime = reduce(lambda x, y: (x + y) / 2, mytimelist)
avg_cnttime = reduce(lambda x, y: (x + y) / 2, cnttimelist)

# The yval position is reversed, but according to the numbers computed, cnt took shorter time than my function.
yval = [avg_cnttime, avg_mytime]
x = ["Me", "Counter"]
plt.figure(figsize=(10,6))
plt.bar(x, yval, color='gold')
plt.xticks(x)
plt.xlabel("Performance")
plt.ylabel("Function Call By")
plt.title("Counter Performance")
plt.show()