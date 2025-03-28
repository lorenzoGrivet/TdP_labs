def palyndrome(word):
    if len(word)==1:
        return True
    else:
        return word[0]==word[-1] and palyndrome(word[1:-1])

def palyndrome2(word):
    if word==word[::-1]:
        return True
    else:
        return False

if __name__=="__main__":
    print(palyndrome("casa"))
    print(palyndrome("civic"))
    print(palyndrome2("civic"))