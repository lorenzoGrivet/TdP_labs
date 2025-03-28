a=open("input")
l_in=a.readlines()
dic={}
lista=[]
for e in l_in:
    lista.append(int(e.strip()))
    dic[int(e.strip())]=0
print()

for i in range(1,101):

    if lista.__contains__(i):
        print(str(i))
    else:
        print(str(i)+"MANCA ******************")

for i in lista:

    if dic[i]==1:
        w="DOPPIO"
        print(w+str(i))
    else:
        dic[i]=1
        w=""
