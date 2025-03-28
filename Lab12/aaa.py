diz={}
diz["b"]=2
diz["c"]=3
diz["a"]=1

diz["d"]=4
altro=diz.items()
for a in altro:
    print(a)
print()
print()
ordinato=sorted(altro,key=lambda x: x[1])
for a in ordinato:
    print(a)