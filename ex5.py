def diccionari(llista):
    dic = {}
    for i,e in enumerate(llista):
        dic[e] = i
    print("De la llista he creat el diccionari {}".format(dic))
          
llista = ['cotxe','casa','vaixell','colom','ca','mussol','clara']
diccionari(llista)