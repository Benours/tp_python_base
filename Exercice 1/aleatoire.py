# 1

from random import *

liste = [1, 2, 3, 4, 5]
print("Un nombre avec randint ", randint(1, 5))
print("Un nombre avec randrange ", randrange(1, 10, 2))
print("Un nombre avec choice ", choice(liste))
shuffle(liste)
print("Un mélange de liste avec shuffle ", liste)