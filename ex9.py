def pot(p):
    r = [x**p for x in range(1,10)]
    print("Les potències elevades dels 10 primers numeros és {}".format(r))

p = int(input("Introdueix un numero al cual voleu elevar la resta: "))
pot(p)
