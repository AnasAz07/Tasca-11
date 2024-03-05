import os

companys = ["Federic","Oscar","Paula","Hugo","Claudia","Jordi","Anas","Alvaro","Clara","Palli","Joan","Marc","GitCalvo","Sebas","Pepe","Joselu","Ayoub","David"]
os.mkdir("/home/cicles/AO/Tasca-11/Prova")
os.chdir("/home/cicles/AO/Tasca-11/Prova")
with open("ex12.txt","w") as f:
    for e in companys:
        f.write(e+"\n")
professors = ["Pep","David","Fela","Lluis","Joan"]
with open("ex12.txt","a+") as f:
    for e in professors:
        f.write(e+"\n")

a = []
with open("ex12.txt","r") as f:
    for e in f:
        c = e.split("\n")
        a.append(c[0])

print(a)