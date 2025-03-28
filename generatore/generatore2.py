import math

def creaPassword(sito):

    nome="lorenzogrivettalocia"
    speciali="n!\"£$%&=()"
    _passw="L0ri"
    alfabeto="abcdefghijklmnopqrstuvwxyz"
    vocali="aeiou"
    numeri="0123456789"

    #numero vocali
    v=0
    for l in sito:
        if l in vocali:
            v+=1

    _passw+=str(speciali[v])

    #prendo prime 4 lettere
    if len(sito)>4:
        s=sito[:4]
        _passw+=s.capitalize()
    else:
        s=sito
        _passw+=s.capitalize()

    _passw+=str(v)

    return _passw
