""" 
Si on fait deux séries de mesures distinctes en des points différents mais 
que l'on voudrait additionner les résultats, il est nécessaire de faire une 
interpolation.
"""


import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Les valeurs mesurées

Xserie1 = np.array([30,40,50,60])
Yserie1 = np.array([120,140,170,230])
Xserie2 = np.array([45,55,60,70,85])
Yserie2 = np.array([25,50,35,-25,-100]) 

# Les fonctions d'interpolation

def fonction1(x):
    """ Première fonction d'interpolation: on renvoie 0 si on est hors du domaine """
    if x < min(Xserie1) or x > max(Xserie1):
        return 0
    else:
        return float(interp1d(Xserie1,Yserie1)(x))

def fonction2(x):
    """ Seconde fonction d'interpolation: on renvoie 0 si on est hors du domaine """
    if x < min(Xserie2) or x > max(Xserie2):
        return 0
    else:
        return float(interp1d(Xserie2,Yserie2)(x))



# Représentations graphiques

plt.plot(Xserie1,Yserie1,'-o',label='serie1')
plt.plot(Xserie2,Yserie2,'-o',label='serie2')

x = np.linspace(30,85)
y = np.array([fonction1(xi) + fonction2(xi) for xi in x])

plt.plot(x,y,label='addition')

plt.legend()

plt.show()
