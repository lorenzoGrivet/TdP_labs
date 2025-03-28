import math

def creaPassword(sito):

    nome="lorenzogrivettalocia"
    speciali="!\"£$%&()="
    _passw=""
    alfabeto="abcdefghijklmnopqrstuvwxyz"
    vocali="aeiou"
    numeri="0123456789"


    #prendo prime 4 lettere
    if len(sito)>4:
        _passw+=sito[:4]
    else:
        _passw+=sito

    #aggiungo carattere speciale
    if len(sito)<11:
        _passw+= speciali[len(sito)-1]

    else:
        n= math.floor(len(sito)/10)
        _passw+=speciali[len(sito)-10*n-1]

    #numero vocali
    i=0
    for l in sito:
        if l in vocali:
            i+=1
    _passw+=str(i)

    #aggiungo corrispondenza consonanti
    if len(sito)>len(nome):
        sito=sito[:len(nome)]
    for s in range(len(sito)):
        if not sito[s] in vocali and not sito[s] in numeri:
            _passw+=nome[s]

    #controllo lunghezza
    i=0
    while len(_passw)<8:


       n=_passw[i]
       if n in alfabeto:
           _passw+= str( int(alfabeto.index(n))+1)
       elif n in speciali:
           _passw+=speciali.index(n)+1
       elif n in numeri:
           if n=="0":
               pass
           else:
               _passw+=alfabeto[int(n)-1]

       i=i+1

    _passw=_passw.capitalize()

    return _passw
