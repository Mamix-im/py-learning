#Largest of 3 numbers

a = int(input("Enter num: "))
b = int(input("Enter num: "))
c = int(input("Enter num: "))

if a > b and a > c :
    print("A is largest")
elif b > c :
    print("B is largest")
else:
    print("C is largest")