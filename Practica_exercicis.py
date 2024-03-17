#Ex 1: Crear una funció que compti la longitud de cada paraula 
#d’una cadena de caràcters que li passem. 
#Utilitzar map. 
#Ex: def lenp(frase): -- 
#retorni una llista amb la longitud de cada paraula de la frase.
'''''
def len_paraula():
    frase = input("Introdueix una frase: ")
    x = frase.split(" ")
    y = list(map(len,x))
    print(y)

#Pr. Principal    
len_paraula()
'''

#Ex 2: Crear una funció que donada una llista de dígits ordenats,
#retorni el número corresponent. 
#Utilitzar reduce. Ex: [3, 4, 1, 5] correspòn al número 3415. 
#Ex: def Passar_a_Numero(llista): retorni el número que corresponen els dígits.
'''''
from functools import reduce
def str_a_numero():
    l = [3,4,1,5]
    x = list(map(lambda x:str(x),l))
    y = reduce(lambda x,y:x+y,x)
    print(y)

#Pr. Principal
str_a_numero()
'''

#Ex 3: Crear una funció que donada una llista de paraules i una lletra, 
#retorni una llista amb les paraules que comencen per la lletra donada. 
#Utilitzar filter. Ex: [“maria”, “manta”, “peu”, “mà”] 
#i li deim que ens retorni totes les que comencen per ‘p’
'''''
def Filtre(l,a):
    x = list(filter(lambda x: x[0] == a.lower() or x[0] == a.upper(),l ))
    return x

#Pr. Principal
l = ['Buena', 'Si', 'Chambales', 'Oscar', 'Boom']
a = 'b'
print(Filtre(l,a))
'''
#Ex 4: Crear una funció que donades dues llistes, 
#les concateni amb un connector. Utilitzar zip. 
#Ex: [‘sub’,’supra’] i [‘campió’ ‘campiona’] i el connector ‘-’, retorni 
#[‘sub-campió’][‘supra-campiona’].







