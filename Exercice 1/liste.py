# 1

liste_vide = []
var = 'a'
liste_rempli = ["A", 1, True, var]

# 2

print(len(liste_vide))
print(len(liste_rempli))

# 3

liste_rempli[0] = "B"
liste_rempli.remove(1)
liste_rempli.append(1)
print(liste_rempli)

# 4

for i in liste_rempli:
    print(i)

for i in range(len(liste_rempli)):
    print(liste_rempli[i])

while i < len(liste_rempli):
    print(liste_rempli[i])
    i += 1

while liste_rempli:
    element = liste_rempli.pop(0)
    print(element)

