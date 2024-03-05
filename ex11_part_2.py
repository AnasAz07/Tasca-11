def imprimir_fitxer(m):
    a = []
    with open(m,"r") as f:
        for e in f:
            c = e.split("\n")
            a.append(c[0])
    print(a)

def afegir_fitxer(m,llista):
    with open(m,"a+") as f:
        for e in llista:
            f.write(e+"\n")


fitxer = "/home/cicles/AO/Tasca-11/ex-11.txt"
llista = ["Federic","Oscar","Hugo","Claudia","Jordi","Anas","Alvaro"]
afegir_fitxer(fitxer,llista)
imprimir_fitxer(fitxer)
