def fizzBuzz(n):
    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    #  Assigner ensuite la valeur à la variable resultat
    if n % 3 == 0:
        if n % 5 == 0:
            print("fizzbuzz")
        else:
            print("fizz")
    else:
        if n % 5 == 0:
            print("buzz")
    resultat = n
    return resultat

if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))