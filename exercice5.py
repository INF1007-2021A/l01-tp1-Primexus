def pointDeRencontre(v1, v2, distance):
    # TODO faites les calculs intermediaires, vous pouvez initialiser des variables locales.
    t = 0
    d1,d2 = v1*t, -v2*t + distance
    while (d1 != d2):
        t+=1
        d1, d2 = v1 * t, -v2 * t + distance

    # TODO calculer la position de rencontre, assignez la valeur à la variable "positionRencontre"
    positionRencontre = v1*t

    return positionRencontre

if __name__ == '__main__':
    v1 = int(input("Entrez v1: "))
    v2 = int(input("Entrez v2: "))
    distance = int(input("Entrez la distance: "))
    print(pointDeRencontre(v1, v2, distance))
