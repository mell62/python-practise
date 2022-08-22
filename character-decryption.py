#This program is to decrypt characters having ASCII values 0-127 using Caeser cipher
word=input("Enter the code:")
distance=int(input("Enter the distance:"))
code=""
for character in word:
    ascii=ord(character)
    cipher=ascii-distance
    if (cipher<0):
       cipher = 128 + cipher
    code+=chr(cipher)
print(code)