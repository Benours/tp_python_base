# 1

from random import *

def index_minimum(t, d, f):
    index_min = d
    for i in range(d + 1, f + 1):
        if t[i] < t[index_min]:
            index_min = i
    return index_min

# 2

def tri_a_bulles(t):
    for i in range(len(t) - 1):
        for j in range(len(t) - 1 - i):
            if t[j + 1] < t[j]:
                t[j + 1], t[j] = t[j], t[j + 1]
                
# Test

'''
tab = [randint(1, 100) for i in range(10)]
print(tab)
print(index_minimum(tab, 0, len(tab) - 1))
tri_a_bulles(tab)
print(tab)
'''