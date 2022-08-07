lowLimit=2
limit=100
while(lowLimit<limit):
    firstNumber=lowLimit*2
    secondNumber=lowLimit*lowLimit-1
    thirdNumber=lowLimit*lowLimit+1
    if thirdNumber>limit:
        break
    print(firstNumber,secondNumber,thirdNumber)
    lowLimit+=1