def divisio(a,b):

    try:
        c = a//b
        print("El resultat de la divisió és {}".format(c))
    
    except ZeroDivisionError:
        print("El segon paràmetre de la divisió no pot ser 0")
    
a = int(input("Introdueix un numero: "))
b = int(input("Introdueix el numero pel cual dividiràs: "))
c = divisio(a,b)