def ajuntar(l,d,c):
    a = []
    for i in range(len(l)):
        a.append(l[i]+c+d[i])
    print("La unio de les llistes és {}".format(a))

l = ['Super','Hiper', 'Mini', 'Maxi']
d = ['women', 'bole', 'mouse', 'boom']
ajuntar(l,d," ")
