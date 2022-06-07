x = int(input("Enter line length: "))
y = input("Vertical or Horizontal: ")

if y == "Vertical":
    for c in range(0,x):
        print ("*")
        
elif y == "Horizontal":
    for a in range(0,x):
       print ("*", end="")