import random 

response = "y"

while response == "y":
    dice_value = random.randint(1,6)

    if(dice_value == 1):
        print("---------")
        print("|       |")
        print("|   O   |")
        print("|       |")
        print("---------")

    elif(dice_value == 2):
        print("---------")
        print("| O     |")
        print("|       |")
        print("|     O |")
        print("---------")

    elif(dice_value == 3):
        print("---------")
        print("| O     |")
        print("|   O   |")
        print("|     O |")
        print("---------")


    elif(dice_value == 4):
        print("---------")
        print("| O   O |")
        print("|       |")
        print("| O   O |")
        print("---------")



    elif(dice_value == 5):
        print("---------")
        print("| O   O |")
        print("|   O   |")
        print("| O   O |")
        print("---------")




    elif(dice_value == 6):
        print("---------")
        print("| O   O |")
        print("| O   O |")
        print("| O   O |")
        print("---------")



    response = input("Press y to roll again and n to exit - ")

print("Goodbye! Thanks for rolling the dice.")
