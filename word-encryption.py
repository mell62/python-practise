#This program uses Caesar cipher
word=input("Enter a single lowercase word:")
distance=int(input("Enter the distance value:"))
code=""
for letter in word:
    ascii=ord(letter)
    cipher=ascii+distance
    if (cipher>ord("z")):
        cipher= ord("a") + (cipher - ord("z")) - 1
    code+=chr(cipher)
print(code)
