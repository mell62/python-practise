#This program is to demonstrate while loop
num=int(input("Enter a number:"))
fact=num
while(num!=0):
    fact=fact*(num-1)
    num-=1
    if(num-1==0):
        break
print("Factorial is", fact) 