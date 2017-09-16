import numpy as np
import matplotlib.pyplot as plt

v = np.array([1, 3, 2, 4])
print(v)
print(type(v))

plt.figure() #créer une figure '''
plt.plot(v) #dessiner la figure'''

#plt.show()  #afficher la figure'''

x = np.array([0, 2, 4, 6])
plt.figure()
plt.plot(x,v, 'r--', label = 'vecteur')
plt.xlabel('x')
plt.ylabel('v')
plt.title('exemple title')
plt.legend(loc='lower right')
#plt.show()
M = np.array([[1, 3, 3], [2, 4,2]])
print(M)
print(M[0,0])
print(M[1,1])
print(type(M))

print(v.shape) # taille d'un vecteur
print(M.shape) # taille de chaque dim d'un vecteur


print(v.ndim) # permet savoir la dimention d'un vecteur
print(M.ndim) # ||

