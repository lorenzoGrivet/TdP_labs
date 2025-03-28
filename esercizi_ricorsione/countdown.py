from time import sleep


def countdown(n):
    counter =n
    while counter >=0:
        print(counter)
        sleep(1)
        counter-=1

def countdown_recursive(n):
    if n<=0:
        print("stop")
    else:
        print(n)
        countdown_recursive(n-1)

if __name__ == "__main__":
    countdown(10)
    countdown_recursive(10)