word=input("Enter the code:")
distance=int(input("Enter the distance:"))
code=""
for letter in word:
    ascii=ord(letter)
    cipher=ascii-distance
    if (cipher<ord("a")):
        cipher=ord("z") - (distance-(ascii-ord("a")+1))
    code+=chr(cipher)
print(code)