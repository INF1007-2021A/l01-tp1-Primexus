def fizzBuzz(n):
    # TODO imprimer la chaine de caractère appropriée avec la fonction print().
    #  Assigner ensuite la valeur à la variable resultat
    if n % 3 == 0:
        if n % 5 == 0:
            type1 = "fizzbuzz"
            return type1
        else:
            type3 = "fizz"
            return type3
    else:
        if n % 5 == 0:
            type2 = "buzz"
            return type2
    resultat = n
    return resultat

if __name__ == '__main__':
    n = int(input("indiquez le nombre: "))
    print(fizzBuzz(n))
