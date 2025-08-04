'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice (snake/water/gun): ")
youDict = {"snake":1, "water":-1, "gun":0}
reverseDict = {1:"snake", -1:"water", 0:"gun"}  
you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if (computer == you):
    print("It's a tie!")

else:
    if(computer == -1 and you == 1):
        print("You win!")

    elif(computer == -1 and you == 0):
        print("You lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer == 1 and you == 0):
        print("You win!")

    elif(computer == 0 and you == -1):
        print("You win!")

    elif(computer == 0 and you == 1):
        print("You lose!")       

    else:
        print("Something went wrong!")               