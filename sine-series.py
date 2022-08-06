import math
degree=int(input("Enter the degree:"))
terms=int(input("Enter the number of terms for sum:"))
degree=math.radians(degree)
answer=degree
term=degree
count=1
for count in range(1,terms):
    term=(-term*degree*degree)/((count*2)*(count*2+1))
    answer=answer+term
print("The sum of the sine series is: %0.2f" %answer)