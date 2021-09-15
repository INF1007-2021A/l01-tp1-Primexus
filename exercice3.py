
def decomposer(secondes):

    # TODO: Assigner à la variable "annees" le nombre d'années
    annees = secondes//(60*60*24*365)
    reste = secondes%(60*60*24*365)

    # TODO: Assigner à la variable "semaines" le nombre de semaines restantes
    semaines = reste//(60*60*24*7)
    reste%=(60*60*24*7)

    # TODO: Assigner à la variable "jours" le nombre de jours restants
    jours = reste//(60*60*24)
    reste%=(60*60*24)
    # TODO: Assigner à la variable "heures" le nombre d'heures restantes
    heures = reste//(60*60)
    reste%=60*60
    # TODO: Assigner à la variable "minute" le nombre de minutes restantes
    minutes = reste//60
    reste%=60
    # TODO: Assigner à la variable "secondes" le nombre de secondes restantes
    secondes = reste
       # TODO: Afficher le nombres d'années, semaines, jours, heures, minutes et secondes
    prompt = f'Cela équivaut à {annees} année(s), {semaines} semaine(s), {jours} jour(s), {heures} heure(s), {minutes} minute(s) et {secondes} seconde(s).'
    print(prompt)
    return (annees ,semaines ,jours ,heures ,minutes ,secondes)

if __name__ == '__main__':
    secondes = int(input("Entrer les secondes: "))
    print(decomposer(secondes))
