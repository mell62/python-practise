decimal=int(input("Enter the decimal number:"))
binary=""
while(decimal>0):
    remainder=decimal%2
    decimal=decimal//2
    binary+=str(remainder)
binary=binary[::-1]
print("The binary equivalent is:", binary)