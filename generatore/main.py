import generatore2

password={}
sito=input("Sito: ")
file = open("password.txt", "r")
righe=file.readlines()

for riga in righe:
    a=riga.split(sep=" - ")
    password[a[0].strip("\n")]=a[1].strip("\n")
file.close()
file= open("password.txt","a")

while sito!= "stop":

    if sito not in password.keys():
        p=generatore2.creaPassword(sito)

        file.write(f"{sito} - {p}\n")

    sito = input("Sito: ")

file.close()
