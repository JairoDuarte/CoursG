
from __future__ import print_function

print("Bonjour tout le monde!") 
a = 1
print(type(a))

test = (3 > 4)
print(test)
print(type(test))
b = 3 / 2 # division entiere

# Partie 2 - La bibliotheque standard et ses modules

print("Partie 2 - La bibliotheque standard et ses modules")


from math import cos, pi
import math as m

x = cos(2 * pi)

print(x)

print(dir(m))

import fractions
a = fractions.Fraction(2, 3)
b = fractions.Fraction(1, 2)
print(a + b)

# Partie 3 - Conteneurs: Chaines de caracteres Listes Tuples Dictionnaires

print("Partie 3 - Conteneurs: Chaines de caracteres Listes Tuples Dictionnaires")

s = 'Bonjour Telecom ParisTech!'
# ou avec " "
s = "Bonjour Telecom ParisTech!"
print(s)
print(type(s))

print("str1",1.0,False,-1j)

nbr = 12
nbr1 = 11.0

print("val1 = %f" % nbr + " val2= %s" % nbr1)
s = "val1 = %f, val2 = %f" % (nbr,nbr1)

print(s)

an = 7 // float(2)

print(an)
print(type(an))
s1 = "%s%s" % ("aaa","0000")
print(s1)