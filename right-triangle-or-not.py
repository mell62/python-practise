side1 = int(input("Enter the length of the first side:"))
side2 = int(input("Enter the length of the second side:"))
side3 = int(input("Enter the length of the third side:"))
square1 = side1**2
square2 = side2**2
square3 = side3**2
if( square1==square2+square3 or square2==square1+square3 or square3==square1+square2 ):
    print("It is a right triangle")
else:
    print("Not a right triangle")