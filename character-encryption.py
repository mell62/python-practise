#This program is to encrypt characters having ASCII values 0-127 using Caeser cipher
string=input("Enter the message:")
distance=int(input("Enter the distance:"))
code=""
for character in string:
    ascii=ord(character)
    cipher=ascii+distance
    if (cipher>127):
        cipher=cipher - 128
    code+=chr(cipher)
print(code)
