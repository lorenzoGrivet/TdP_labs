def binomial(n,m):
    if m==n or m==0:
        return 1
    else:
        return binomial(n-1,m-1) + binomial(n-1,m)


if __name__=="__main__":
    print(binomial(5,3))
    # print(scipy.special.binom(5,3))