# 1

i = 1
while i < 101:
    print(i, end="; ")
    i = i + 1
print()
for j in range(1, 101):
    print(j, end="; ")

# 2

from turtle import *

'''color('red', 'yellow')
begin_fill()
k = 0
while k < 4:
    forward(200)
    left(90)
    k = k + 1
k = 0
left(180)
while k < 3:
    forward(200)
    right(120)
    k = k + 1
end_fill()
done()'''

def figure_geo(nombre_cote = 3, taille = 100):
    iter = 0
    begin_fill()
    while iter < nombre_cote:
        forward(taille)
        left(360 / nombre_cote)
        iter = iter + 1
    end_fill()
    done()

figure_geo(10, 50)