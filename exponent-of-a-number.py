#This program is to demonstrate for loop
num=int(input("Enter the number:"))
exp=int(input("Enter the power:"))
product=1
for count in range(exp):
    product=product*num
    print(product, end=" ")
print("\nThe answer is", product)
