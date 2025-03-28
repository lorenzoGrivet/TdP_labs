import translator as tr

t = tr.Translator()

diz=t.loadDictionary("dictionary.txt") #diz è un oggetto!!!!

while(True):

    t.printMenu()

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print()
        inserimento = input("inserire inserimento: ")
        dizio=t.handleAdd(inserimento,diz)
        diz=dizio

        pass
    if int(txtIn) == 2:
        parola=input("inserire ricerca: ")
        risultato=t.handleTranslate(parola,diz)
        print(risultato)
        pass
    if int(txtIn) == 3:
        parola = input("inserire ricerca: ")
        risultato=t.handleWildCard(parola,diz)
        print(risultato)
        pass
    if int(txtIn) == 4:
        break
