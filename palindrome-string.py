string=input("Enter the string:")
string=string.lower()
reverse=string[::-1]
if(reverse==string):
    print("String is palindrome")
else:
    print("String is not palindrome")