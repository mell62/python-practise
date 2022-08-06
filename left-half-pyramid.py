count=int(input("Enter maximum length of pyramid:"))
for firstLoop in range(1,count+1):
    for secondLoop in range(1,firstLoop+1):
        print(secondLoop,end=" ")
    print()