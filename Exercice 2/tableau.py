# a

# 1

liste = [0, 80, 8, 19, 9, 72, 9]

def moy_tab(liste):
    som = 0
    for i in liste:
        som = som + i
    moy = som / len(liste)
    return moy

print(moy_tab(liste))

# 2

def nombre_occurence(element, liste):
    occu = 0
    for i in liste:
        if element == i:
            occu = occu + 1
    return occu

print(nombre_occurence(4, liste))

# 3

def sup_10(liste):
    sup = 0
    for i in liste:
        if i >= 10:
            sup = sup + 1
    return sup

print(sup_10(liste))

# 4

def max_element(liste):
    if len(liste) < 1:
        return "WARN: Liste vide."
    max = liste[0]
    for i in liste:
        if i > max:
            max = i
    return max

print(max_element(liste))

# 5

def find_element(element, liste):
    find = False
    for i in liste:
        if i == element:
            find = True
            break
    return find

print(find_element(9, liste))
print(find_element(3, liste))

# b

# 1

from random import *

def create_tab(n):
    tab = []
    for i in range(n + 1):
        tab.append(randint(-100, 100))
    return tab

tab_test_1 = create_tab(1000)
print(tab_test_1)

# 2

def create_tab_n_entier(n):
    tab = []
    for i in range(n + 1):
        tab.append(i)
    shuffle(tab)
    return tab

tab_test_2 = create_tab_n_entier(1000)
print(tab_test_2)

# time

# 1

from time import *

start = time()

moy_tab(tab_test_2)

stop = time()

print("La fonction moy_tab a mis ", stop - start, " secondes")

start = time()

find_element(0, tab_test_2)

stop = time()

print("La fonction moy_tab a mis ", stop - start, " secondes")