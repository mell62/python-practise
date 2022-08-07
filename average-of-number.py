#This program is to demonstrate while loop
sum=0
count=0
while True:
    number=input("Enter the number or press Enter to finish:")
    if(number==""):
        break
    sum+=float(number)
    count+=1
if(count>0):
    print("The average is: %0.2f" %(sum/count))
