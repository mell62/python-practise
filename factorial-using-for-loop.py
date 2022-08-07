#This program is to demonstrate for loop
num=int(input("Enter the number"))
fact=1
for count in range(num):
    fact=fact*num
    num=num-1
    print(fact, end=" ")
print("Factorial is", fact)
