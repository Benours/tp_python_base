from random import *

tableau_prenom = ["Jean", "Marc", "Luc", "Pierre", "Paul", "Jacques", "Thomas", "Nicolas", "François", "Michel"]
tableau_nom = ["Dupont", "Durand", "Dubois", "Moreau", "Lefebvre", "Leroy", "Roux", "David", "Bertrand", "Morel"]

'''
class Etudiant:
    def __init__(self):
        self.nom = choice(tableau_nom)
        self.prenom = choice(tableau_prenom)
        self.note_francais = randint(1, 20)
        self.note_maths = randint(1, 20)
        self.note_histoire = randint(1, 20)
        self.note_geo = randint(1, 20)
    
    def moyenne(self):
        return (self.note_francais + self.note_maths + self.note_histoire + self.note_geo) / 4

class Promotion:
    def __init__(self):
        self.liste_etudiant = []
        for i in range(10, 30):
            self.liste_etudiant.append(Etudiant())
    
    def moyenne_matiere(self, nom_matiere):
        somme = 0
        for etudiant in self.liste_etudiant:
            somme += getattr(etudiant, nom_matiere)
        return somme / len(self.liste_etudiant)
    
    def note_max(self, nom_matiere):
        note_max = 0
        for etudiant in self.liste_etudiant:
            note = getattr(etudiant, nom_matiere)
            if note > note_max:
                note_max = note
        return note_max
    
promo = Promotion()
for etudiant in promo.liste_etudiant:
    print(etudiant.nom, etudiant.prenom, etudiant.note_francais, etudiant.note_maths, etudiant.note_histoire, etudiant.note_geo, etudiant.moyenne())

print(promo.moyenne_matiere("note_francais"))
print(promo.note_max("note_francais"))
print(promo.moyenne_matiere("note_maths"))
print(promo.note_max("note_maths"))
print(promo.moyenne_matiere("note_histoire"))
print(promo.note_max("note_histoire"))
print(promo.moyenne_matiere("note_geo"))
print(promo.note_max("note_geo"))
'''

class Etudiant:
    def __init__(self, nombre_matieres):
        self.nom = choice(tableau_nom)
        self.prenom = choice(tableau_prenom)
        self.nombre_matieres = nombre_matieres
        for i in range(nombre_matieres):
            setattr(self, "note_" + str(i), randint(1, 20))
    
    def moyenne(self):
        somme = 0
        for i in range(self.nombre_matieres):
            somme += getattr(self, "note_" + str(i))
        return somme / self.nombre_matieres
    
class Promotion:
    def __init__(self, nombre_matieres):
        self.liste_etudiant = []
        self.nombre_matieres = nombre_matieres
        for i in range(10, 30):
            self.liste_etudiant.append(Etudiant(nombre_matieres=nombre_matieres))
    
    def moyenne_matiere(self, nom_matiere):
        somme = 0
        for etudiant in self.liste_etudiant:
            somme += getattr(etudiant, nom_matiere)
        return somme / len(self.liste_etudiant)
    
    def note_max(self, nom_matiere):
        note_max = 0
        for etudiant in self.liste_etudiant:
            note = getattr(etudiant, nom_matiere)
            if note > note_max:
                note_max = note
        return note_max
    
promo = Promotion(10)
for etudiant in promo.liste_etudiant:
    print(etudiant.nom, etudiant.prenom)
    for i in range(promo.nombre_matieres):
        print(" - Ceci est la note de la matière", i, ":", getattr(etudiant, "note_" + str(i)))
    print(" - Ceci est la moyenne ", etudiant.moyenne())

for i in range(promo.nombre_matieres):
    print("Ceci est la matière", i, end=" :\n")
    print(" - Ceci est la moyenne", promo.moyenne_matiere("note_" + str(i)))
    print(" - Ceci est la note maximale", promo.note_max("note_" + str(i)))