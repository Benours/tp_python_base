# 1

def find_in_sort_tab(t, e):
    for i in range(len(t)):
        if t[i] == e:
            return i
    return "WARN: Element non trouvé"
'''
tab_sort = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_in_sort_tab(tab_sort, 5))
print(find_in_sort_tab(tab_sort, 11))
'''
# 2

def find_dichotomique(t, e):
    d = 0
    f = len(t) - 1
    while d <= f:
        m = (d + f) // 2
        if t[m] == e:
            return m
        elif t[m] < e:
            d = m + 1
        else:
            f = m - 1
    return "WARN: Element non trouvé"
    
'''
print(find_dichotomique(tab_sort, 5))
print(find_dichotomique(tab_sort, 11))
'''
# 3

def insertion(e, t, n):
    i = n - 2
    while i >= 0 and t[i] > e:
        t[i + 1] = t[i]
        i -= 1
    t[i + 1] = e
'''
print(tab_sort)
insertion(9, tab_sort, len(tab_sort))
print(tab_sort)
'''