import spellchecker

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()

        risultato = sc.handleSentence(txtIn,"italian")

        comandi=["Contains:","Linear:","Dicotomic:"]
        a=0
        for i in risultato:
            print(f"Lista parole errate usando {comandi[a]}")
            a+=1

            for w in i[0]:
                print(w)

            print(f"Numero parole errate: {len(i[0])}")
            print(f"Tempo impiegato per il calcolo: {i[1]}")
            print ("--------------------------------------------------------")

        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        risultato=sc.handleSentence(txtIn,"english")

        comandi = ["Contains:", "Linear:", "Dicotomic:"]
        a = 0
        for i in risultato:
            print(f"Lista parole errate usando {comandi[a]}")
            a += 1

            for w in i[0]:
                print(w)

            print(f"Numero parole errate: {len(i[0])}")
            print(f"Tempo impiegato per il calcolo: {i[1]}")
            print("--------------------------------------------------------")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        risultato=sc.handleSentence(txtIn,"spanish")
        comandi = ["Contains:", "Linear:", "Dicotomic:"]
        a = 0
        for i in risultato:
            print(f"Lista parole errate usando {comandi[a]}")
            a += 1

            for w in i[0]:
                print(w)

            print(f"Numero parole errate: {len(i[0])}")
            print(f"Tempo impiegato per il calcolo: {i[1]}")
            print("--------------------------------------------------------")
        continue

    if int(txtIn) == 4:
        break


