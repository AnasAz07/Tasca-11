def llegir_llista():
    a = 'l'
    l = []
    while a!= '.':
        a = input("Introduce la lista, para terminarla mete un . : ")
        if a!= '.':
            l.append(a)
        else:
            return l
        
def filtre_inicial(x,a):
    l = list(filter(lambda y: y[0] == a.lower() or y[0] == a.upper(), x))
    return l

x = llegir_llista()
a = "m"
print(filtre_inicial(x,a))