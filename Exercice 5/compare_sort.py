from pygnuplot import gnuplot

# 1

tab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def copie(t):
    return [x for x in t]
'''
new_tab = copie(tab)
new_tab[0] = 0
print(tab)
print(new_tab)
'''
# 2

def inverse(t):
    return [t[len(t) - 1 - i] for i in range(len(t))]
'''
new_tab = inverse(tab)
print(tab)
print(new_tab)
'''

# 3

def tableau_premiers_entiers(n):
    return [i for i in range(n)]

import random
def tableau_premiers_entiers_melanges(n):
    return random.sample(tableau_premiers_entiers(n), n)

def tableau_premiers_entiers_inverses(n):
    return inverse(tableau_premiers_entiers(n))
'''
new_tab = tableau_premiers_entiers(10)
print(new_tab)
new_tab = tableau_premiers_entiers_melanges(10)
print(new_tab)
new_tab = tableau_premiers_entiers_inverses(10)
print(new_tab)
'''

# 4

def ligne_dans_fichier(f, n, t):
    f.write(str(n) + "\t" + str(t) + "\n")
    
# 5

import time

def tri_a_bulles(t):
    for i in range(len(t) - 1):
        for j in range(len(t) - 1 - i):
            if t[j + 1] < t[j]:
                t[j + 1], t[j] = t[j], t[j + 1]
    
def temps_tri_bulles(t):
    new_tab = copie(t)
    start = time.time()
    tri_a_bulles(new_tab)
    end = time.time()
    return end - start

# 6

def stats_melange(nmin, nmax, pas, fois):
    with open("temps_moyens_mel.dat", "w") as file:
        for taille in range(nmin, nmax + 1, pas):
            temps_total = 0
            for _ in range(fois):
                tableau = tableau_premiers_entiers_melanges(taille)
                
                temps_execution = temps_tri_bulles(tableau)
                
                temps_total += temps_execution
            
            temps_moyen = temps_total / fois
            ligne_dans_fichier(file, taille, temps_moyen)
'''
stats_melange(100, 1000, 100, 10)
'''
# 7

def stats_ordonne(nmin, nmax, pas, fois):
    with open("temps_moyens_ord.dat", "w") as file:
        for taille in range(nmin, nmax + 1, pas):
            temps_total = 0
            for _ in range(fois):
                tableau = tableau_premiers_entiers(taille)
                
                temps_execution = temps_tri_bulles(tableau)
                
                temps_total += temps_execution
            
            temps_moyen = temps_total / fois
            ligne_dans_fichier(file, taille, temps_moyen)
'''            
stats_ordonne(100, 1000, 100, 10)
'''
# 8

def stats_inverse(nmin, nmax, pas, fois):
    with open("temps_moyens_inv.dat", "w") as file:
        for taille in range(nmin, nmax + 1, pas):
            temps_total = 0
            for _ in range(fois):
                tableau = tableau_premiers_entiers_inverses(taille)
                
                temps_execution = temps_tri_bulles(tableau)
                
                temps_total += temps_execution
            
            temps_moyen = temps_total / fois
            ligne_dans_fichier(file, taille, temps_moyen)
'''            
stats_inverse(100, 1000, 100, 5)
'''
# 10

def index_minimum(t, d, f):
    index_min = d
    for i in range(d + 1, f + 1):
        if t[i] < t[index_min]:
            index_min = i
    return index_min

def tri_extraction(t):
    for i in range(len(t) - 1):
        index_min = index_minimum(t, i, len(t) - 1)
        t[i], t[index_min] = t[index_min], t[i]
        
def temps_tri_extraction(t):
    new_tab = copie(t)
    start = time.time()
    tri_extraction(new_tab)
    end = time.time()
    return end - start
        
def insertion(e, t, n):
    i = n - 2
    while i >= 0 and t[i] > e:
        t[i + 1] = t[i]
        i -= 1
    t[i + 1] = e
    
def tri_insertion(t):
    for i in range(1, len(t)):
        insertion(t[i], t, i + 1)
        
def temps_tri_insertion(t):
    new_tab = copie(t)
    start = time.time()
    tri_insertion(new_tab)
    end = time.time()
    return end - start
        
def tri_rapide(tableau):
    pass
    
        
def temps_tri_rapide(t):
    new_tab = copie(t)
    start = time.time()
    tri_rapide(new_tab)
    end = time.time()
    return end - start

def stats_melanges_gen(nmin, nmax, pas, fois, type_tri, nom_tri):
    with open("temps_moyens_mel_gen_" + nom_tri + ".dat", "w") as file:
        for taille in range(nmin, nmax + 1, pas):
            temps_total = 0
            for _ in range(fois):
                tableau = tableau_premiers_entiers_melanges(taille)
                
                temps_execution = type_tri(tableau)
                
                temps_total += temps_execution
            
            temps_moyen = temps_total / fois
            ligne_dans_fichier(file, taille, temps_moyen)
'''
stats_melanges_gen(100, 1000, 100, 10, temps_tri_bulles, "bulles")
stats_melanges_gen(100, 1000, 100, 10, temps_tri_extraction, "extraction")
stats_melanges_gen(100, 1000, 100, 10, temps_tri_insertion, "insertion")
# stats_melanges_gen(100, 1000, 100, 10, temps_tri_rapide)
'''
def stats_ordonnes_gen(nmin, nmax, pas, fois, type_tri, nom_tri):
    with open("temps_moyens_ord_gen_" + nom_tri + ".dat", "w") as file:
        for taille in range(nmin, nmax + 1, pas):
            temps_total = 0
            for _ in range(fois):
                tableau = tableau_premiers_entiers(taille)
                
                temps_execution = type_tri(tableau)
                
                temps_total += temps_execution
            
            temps_moyen = temps_total / fois
            ligne_dans_fichier(file, taille, temps_moyen)
'''            
stats_ordonnes_gen(100, 1000, 100, 10, temps_tri_bulles, "bulles")
stats_ordonnes_gen(100, 1000, 100, 10, temps_tri_extraction, "extraction")
stats_ordonnes_gen(100, 1000, 100, 10, temps_tri_insertion, "insertion")
# stats_ordonnes_gen(100, 1000, 100, 10, temps_tri_rapide)
'''
def stats_inverses_gen(nmin, nmax, pas, fois, type_tri, nom_tri):
    with open("temps_moyens_inv_gen_" + nom_tri + ".dat", "w") as file:
        for taille in range(nmin, nmax + 1, pas):
            temps_total = 0
            for _ in range(fois):
                tableau = tableau_premiers_entiers_inverses(taille)
                
                temps_execution = type_tri(tableau)
                
                temps_total += temps_execution
            
            temps_moyen = temps_total / fois
            ligne_dans_fichier(file, taille, temps_moyen)
'''            
stats_inverses_gen(100, 1000, 100, 10, temps_tri_bulles, "bulles")
stats_inverses_gen(100, 1000, 100, 10, temps_tri_extraction, "extraction")
stats_inverses_gen(100, 1000, 100, 10, temps_tri_insertion, "insertion")
# stats_inverses_gen(100, 1000, 100, 10, temps_tri_rapide)
'''
# 11

import gnuplotlib as gp
import numpy as np


def plot_graph(type_tab):
    files = ['temps_moyens_'+type_tab+'_gen_bulles.dat', 'temps_moyens_'+type_tab+'_gen_extraction.dat', 'temps_moyens_'+type_tab+'_gen_insertion.dat']
    data = []

    for filename in files:
        x, y = np.loadtxt(filename, unpack=True)
        data.append((x, y))

    gp.plot(*data, _with='lines', terminal='pngcairo', output='output'+type_tab+'.png')


# Call the plot_graph() function to generate the graph and save as a PNG file
plot_graph('inv')
plot_graph('mel')
plot_graph('ord')
