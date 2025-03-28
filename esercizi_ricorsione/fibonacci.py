import time
from functools import lru_cache,cache

class Fibonacci:
    def __init__(self):
        self.cache= {0:0, 1:1}

    def calcola_elemento_cache(self,n):
        #
        # if n==0:
        #     return 0
        # if n==1:
        #     return 1

        if self.cache.get(n) is not None:
            return self.cache[n]
        else:
            self.cache[n]=self.calcola_elemento_cache(n-2)+self.calcola_elemento_cache(n-1)
            return self.cache[n]

    def calcola_elemento_lru(self,n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            self.cache[n]= self.calcola_elemento_lru(n-1)+self.calcola_elemento_lru(n-2)
            return self.cache[n]

if __name__=="__main__":
    fib=Fibonacci()
    n=3

    start=time.time()
    a=fib.calcola_elemento_cache(n)
    end=time.time()
    tempo=end-start

    print(f"Risultato: {a}, tempo: {tempo}")

    start2 = time.time()
    b = (fib.calcola_elemento_lru(n))
    end2 = time.time()
    tempo2=end2-start2

    print(f"Risultato: {b}, tempo: {tempo2}")

