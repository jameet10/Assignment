#Pattern -2 Program
def pattern():
    n=input("Enter the last letter")
    ch=ord(n)
    for i in range(65,ch+1):
        for j in range(65,65+ch-i+1):
            print(chr(j),end="")
        for l in range(1,2*(i-65)+1):
            print(" ",end="")   
        for k in range(ch-i+65,64,-1):
            if(k==ch):
               continue;
            print(chr(k),end="")
        print()
