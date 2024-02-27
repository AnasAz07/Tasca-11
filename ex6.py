def coincidir(llista):
    l = []
    for i,e in enumerate(llista):
        if e == i:
            l.append(e)
    print("Els elements que coincideixen en la seva posició son {}".format(l))

l = [3, 7, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
coincidir(l)