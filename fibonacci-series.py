terms=int(input("Enter the number of terms:"))
firstTerm=0
secondTerm=1
print(firstTerm, secondTerm, end=" ")
loopElement=1
while(loopElement<=terms-2):
    newTerm=firstTerm+secondTerm
    print(newTerm, end=" ")
    firstTerm=secondTerm
    secondTerm=newTerm
    loopElement+=1

