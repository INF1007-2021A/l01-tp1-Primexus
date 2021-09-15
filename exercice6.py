import matplotlib.pyplot as plt
import math
import numpy as np


def trouverAngle(nombreComplexe):
    return np.angle(nombreComplexe, deg=True)

def trouverModule(nombreComplexe):
    # TODO: Calculer le module du nombre complexe et l'assigner dans "module"
    module = ((nombre.real)**2+(nombre.imag)**2)**(1/2)

    return module



def effectuerRotation(nombreComplexe, angle_rotation, trouverModule):

    module = trouverModule(nombreComplexe)
    angle = trouverAngle(nombreComplexe)

    # TODO: Afficher le module et l'angle du nombre complexe (3 decimales de précision)
    print("Le module est de", round(module,3), "et l'angle est de", round(angle,3),"°")

    # TODO: Calculer le nouveau nombre complexe après rotation, assigner le nouveau nombre complexe à la variable 'resultat'
    z = complex(math.cos(angle), math.sin(angle))
    resultat = nombre*z
    nouveauModule = trouverModule(resultat)
    nouvelAngle = trouverAngle(resultat)

    # TODO : Afficher le nouveau module et le nouvel angle du nombre complexe après rotation (3 decimales de précision)
    print("Le nouveau module est de", round(nouveauModule, 3), "et l'angle est de", round(nouvelAngle, 3), "°")
    return resultat


def dessiner(number, label):
    if number != None:
        plt.polar([0, math.radians(trouverAngle(number))], [0, trouverModule(number)], marker='o', label=label)

if __name__ == '__main__':
    nombre = complex(input("Veuillez entrer un nombre complexe de votre choix sous la forme a+bj (exemple: 1+2j): "))
    rotation = float(input("Veuillez entrer un angle de rotation (en degres) de votre choix (exemple: 87): "))

    try:
        resultat = effectuerRotation(nombre, rotation, trouverModule)
    except Exception as e:
        print(e)
        resultat = None

    dessiner(nombre, 'Avant rotation')
    dessiner(resultat, 'Après rotation')
    plt.legend()
    plt.show()
