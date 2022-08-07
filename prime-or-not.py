num=int(input("Enter the number to checked:"))
factor=2
prime=True
while(factor<=num/2):
    if(num%factor==0):
        prime=False
        break
    factor+=1
if(prime):
    print("It is a prime number")
else:
    print("It is not a prime number")

