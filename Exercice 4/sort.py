# 1

from algo_tab_unsort import index_minimum

def tri_extraction(t):
    for i in range(len(t) - 1):
        index_min = index_minimum(t, i, len(t) - 1)
        t[i], t[index_min] = t[index_min], t[i]
        
tab_unsort = [5, 2, 8, 1, 9, 3, 6, 4, 7, 10]
print(tab_unsort)
tri_extraction(tab_unsort)
print(tab_unsort)

# 2

from algo_tab_sort import insertion

def tri_insertion(t):
    for i in range(1, len(t)):
        insertion(t[i], t, i + 1)

tab_unsort = [5, 2, 8, 1, 9, 3, 6, 4, 7, 10]
print(tab_unsort)
tri_insertion(tab_unsort)
print(tab_unsort)
