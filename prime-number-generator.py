print("Enter the range:")
firstTerm=int(input("Enter the lower range:"))
secondTerm=int(input("Enter the upper range:"))
for loop in range (firstTerm,secondTerm+1):
    factor=2
    prime=True
    while(factor<=loop/2):
        if(loop%factor==0):
            prime=False
            break
        factor+=1
    if(prime):
        print(loop, end=" ")


