def fizzBuzz(n):
    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    #  Assigner ensuite la valeur à la variable resultat
    n = input("Donnez un nombre n :" )
    if n%3 == 0:
        print("fizz")
    if n%5 == 0:
        print("buzz")
    resultat =
    return resultat

if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))
