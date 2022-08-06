count=10
for mainLoop in range(1,count+1):
    for blankLoop in range(1,count-mainLoop+1):
        print(" ",end="")
    for leftnumberLoop in range(1,mainLoop+1):
        print(leftnumberLoop, end="")
    for rightnumberLoop in range(mainLoop-1,0,-1):
        print(rightnumberLoop, end="")
    print()