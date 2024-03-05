class Animal():
    def __init__(self, atribut, edat):
        self.atribut=atribut
        self.edat=edat
    def xerrar(self):
        pass
    def mourem(self):
        pass
    def qui_soc(self):
        print("Soc un animal")

class Cavall(Animal):
    def xerrar(self):
        print("Íiiiiiiiiiiiiii")
    def mourem(self):
        print("Em moc a trot")
    def qui_soc(self):
        print("Sóc un Cavall")
class Dofi(Animal):
    def xerrar(self):
        print("IchIchIchIch")
    def mourem(self):
        print("Em moc nadant")
    def qui_soc(self):
        print("Sóc un Dofí")
class Abella(Animal):
    def xerrar(self):
        print("Zzzzzzzzzzzzzz")
    def mourem(self):
        print("Em moc volant")
    def qui_soc(self):
        print("Sóc una Abella")
class Huma(Animal):
    def __init__(self, nom, atribut, edat):
        self.nom = nom
        self.atribut = atribut
        self.edat = edat
    def xerrar(self):
        print("Hola, xerram utilitzant un idioma")
    def mourem(self):
        print("Em moc caminant")
    def qui_soc(self):
        print("Sóc un Humà")
class Centaure(Huma, Animal):
    def xerrar(self):
        print("Hola, xerram utilitzant un Idioma")
    def mourem(self):
        print("Em moc a trot")
    def qui_soc(self):
        print("Sóc un Centaure")


class Fillet(Huma):
    def __init__(self, nom, atribut, edat, llpares):
        self.nom = nom
        self.atribut = atribut
        self.edat = edat
        self.llpares = llpares
    def xerrar(self):
        print("UeeeeeUeeeeee")
    def mourem(self):
        print("Em moc gatejant")
    def qui_soc(self):
        print("Sóc un Fillet")

class Xou(Animal):
    def xerrar(self):
        print("Xou")
    def mourem(self):
        print("Em moc fent xou")
    def qui_soc(self):
        print("Sóc un Xou")

#Programa Principal

a = [Cavall("Marró","4"),
     Dofi("Gris","10"),
     Abella("Negre i Groga","0,5"),
     Huma("Sibila","Cristià","7"),
     Centaure("Fiona","Marró","18"),
     Fillet("Jordi","Moreno","9",["Fiona","Marc"]),
     Xou("xou","7")]

for e in a:
    e.xerrar()
    e.mourem()
    e.qui_soc()
