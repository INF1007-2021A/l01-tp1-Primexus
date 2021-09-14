n = int(input("Enter a number : "))
if n % 3 == 0:
    if n % 5 == 0:
        print("fizzbuzz")
    else:
        print("fizz")
else:
    if n % 5 == 0:
        print("buzz")
