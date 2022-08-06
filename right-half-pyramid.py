count=9
for mainLoop in range(1,count+1):
    for blankLoop in range(1,count-mainLoop+1):
        print(" ",end="")
    for numberLoop in range(1,mainLoop+1):
        print(numberLoop,end="")
    print()