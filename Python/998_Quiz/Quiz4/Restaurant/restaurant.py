import random
list = ["In N Out", "KFC", "Pho 22"]
num1 = ["Chesse Burger", "French Fries", "Soda", "Double Chesse Burger"]
num2 = ["Grilled Chicken", "Garlic Chicken", "Spicy, Hot Chicken"]
num3 = ["Plain Noddle", "Pork Noodle", "Egg Roll", "Fried Rice"]

y = random.randrange(0,4)
x = input("Which restaurant? ")
if x == "In N Out":
    print (num1)
    print (num1[random.randrange(4)])
elif x == "KFC":
    print (num2)
    print (num2[random.randrange(4)])
elif x == "Pho 22":
    print (num3)
    print (num3[random.randrange(4)])
else:
    print("Try Again")
