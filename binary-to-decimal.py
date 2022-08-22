
binary=input("Enter the binary number:")
length=len(binary)
exponent=length-1
decimal=0
for digit in binary:
    product=int(digit)*(2**(exponent))
    decimal+=product
    exponent-=1
print(decimal)
