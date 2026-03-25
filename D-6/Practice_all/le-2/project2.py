#Simple Calculator

a = int(input("Enter frist number: "))
b = int(input("Enter second number: "))


op = input("Enter operation(+,-,*,/): ")

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op =="*":
    print(a*b)
elif op == "/":
   print(a / b)
else:
    print("Invalid")

