firstNumber=int(input("Enter the first number:"))
secondNumber=int(input("Enter the second number:"))
while(secondNumber>0):
    remainder=firstNumber%secondNumber
    firstNumber=secondNumber
    secondNumber=remainder
print("GCD is", firstNumber)