
def prime(n):
    c=1
    for i in range(2,((n//2)+1)):
        if n%i==0:
            c=0
    return c;

def output():
    for i in range(1,101):
        if prime(i):
            print(i)

        
