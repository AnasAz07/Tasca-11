def len_paraula():
    x = input("Introdueix una frase: ")
    y = list(x.split(" "))
    z = list(map(len,y))
    print(z)

len_paraula()
    
