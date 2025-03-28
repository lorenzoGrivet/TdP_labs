
class Dichotomic:

    def __init__(self):
        self.soluzione=[]

    def solve(self,input_list,index_low,index_high, val):
        if index_high< index_low:
            return False

        if index_low==index_high:
            if input_list[index_low] == val:
                self.soluzione.append(val)
                return True
            else:
                return False
        else:
            i = (index_high-index_low) // 2
            return self.solve(input_list, index_low,i,val) or self.solve(input_list,i+1,index_high, val)


def dichotomic(input_list,val):

    if len(input_list)==1:
        if input_list[0]==val:
            return True
        else:
            return False
    else:
        i = len(input_list)//2
        return dichotomic(input_list[:i],val) or dichotomic(input_list[i:],val)

sequenza=[1,2,3,4,5,6]
print(dichotomic(sequenza,2))
print(dichotomic(sequenza,10))
print()
dic=Dichotomic()
val=4
print(f"{dic.solve(sequenza,0,len(sequenza)-1,val)}, l'indice è: {dic.soluzione}")
