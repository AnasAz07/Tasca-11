def llegir_llista():
    a = 'l'
    l = []
    while a!= '.':
        a = input("Introduce la lista, para terminarla mete un . : ")
        if a!= '.':
            l.append(int(a))
        else:
            return l
        
def filtre_inicial():
    
