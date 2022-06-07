item = int(input("How many items are you purchasing? "))

total = 0
for x in range (0,item):
    name = input("What is the item? ")
    price = float(input("How much is it? "))
    print("Thanks for purchasing " + name)
    total = total + price

print ("Your total is: " + str(total))