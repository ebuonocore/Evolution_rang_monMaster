import matplotlib.pyplot as plt
import numpy as np

def creation_couleurs(nb_col:int):
    """ Renvoie une liste de nb_col couleurs

    Args:
        nb_col (int): Nombre de couleurs dans la liste à renvoyer
    """
    c = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    if len(c) >= nb_col:
        return c[:nb_col]
    else:
        m = nb_col//len(c)
        return c*(m+1)


def date_obtention(evolution:list)->int|None:
    """ Renvoie le nombre de jours avant d'atteindre l'obtention.
        Renvoie None si la pente est positive.

    Args:
        evolution (list): Evolution du classement dans la liste d'attente

    Returns:
        int: nombre d'itérations estimée avant obtention
    """
    from math import ceil
    nb_jours = len(evolution)
    pente = (evolution[-1] - evolution[0])/(nb_jours-1)
    if pente > 0:
        return None
    return ceil(-evolution[-1]/pente)

masters = {"Notaire Dauphine":[47,44,39,32],
           "Notaire Nice":[71,53,40,29],
           "Affaire PC":[47,39,31,22],
           "Fiscal PC":[197, 153,135,113],
           "Notarial PC":[152,133,120,107],
           "Fiscal Nanterre":[298,278,258,235],
           "Notaire Nanterre":[37, 29,23,20]
}

couleurs = creation_couleurs(len(masters))
print(couleurs)
plt.style.use('_mpl-gallery')
plt.axis([0,30,0,300])
n = 0
fig, ax = plt.subplots()
for k,v in masters.items():
    date = date_obtention(v)
    print(k,"->",  date_obtention(v))
    x = list(range(len(v)))
    nb_elements = len(v) + date
    x2 = list(range(nb_elements))
    a = (v[-1]-v[0])/(len(v)-1)
    b = v[0]
    y2 = [a*i+b for i in x2]
    ax.scatter(x, v, c=couleurs[n])
    ax.plot(x2, y2, '-', linewidth=1, c=couleurs[n], label = k)
    ax.legend()
    n += 1
plt.show()