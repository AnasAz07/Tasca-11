def imprimir_fitxer(m):
    a = []
    with open(m,"r") as f:
        for e in f:
            c = e.split("\n")
            a.append(c[0])
    print(a)

fitxer = "/home/cicles/AO/Tasca-11/ex-11.txt"
imprimir_fitxer(fitxer)
