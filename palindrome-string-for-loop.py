#this program is to demonstrate string reversal using for loop
string=input("Enter the string:")
string=string.lower()
reverse=""
for index in range(len(string)-1,-1,-1):
    reverse=reverse+string[index]
if(reverse==string):
    print("String is palindrome")
else:
    print("String is not palindrome")