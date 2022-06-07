x = int(input("Enter a number: "))
z = str(input("Enter an operation: "))
y = int(input("Enter the second number: "))
if z == "+":
    print(x+y)
elif z == "-":
    print(x-y)
elif z == "*":
    print(x*y)
elif z == "/":
    print (x/y)
else:
    print ("error")
