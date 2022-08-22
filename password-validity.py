"""Write a Python program to check the validity of a password given by the
user.
The Password should satisfy the following criteria:
1. Contains at least one letter between a and z
2. Contains at least one number between 0 and 9
3. Contains at least one letter between A and Z
4. Contains at least one special character from $, #, @
5. Minimum length of password: 6""" 

password=input("Enter password:")
lowerCase=0
upperCase=0
number=0
spChar=0
for character in password:
    if len(password)>=6:
        if(character.islower()):
            lowerCase+=1
        elif(character.isupper()):
            upperCase+=1
        elif(character.isdigit()):
            number+=1
        elif(character=="$" or character=="#" or character=="@"):
            spChar+=1
if (lowerCase>=1 and upperCase>=1 and number>=1 and spChar>=1):
    print("Password is valid")
else:
    print("Password is invalid")
