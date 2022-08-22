word=input("Enter a single lowercase word:")
distance=int(input("Enter the distance value:"))
code=""
for letter in word:
    ascii=ord(letter)
    cipher=ascii+distance
    if (cipher>ord("z")):
        cipher= ord("a") + distance - (ord("z")-ascii+1)
    code+=chr(cipher)
print(code)
