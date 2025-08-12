import random
n = random.randint(1, 100)

a = -1
guesses = 1
while a!=n:
    
    a = int(input("Guess a number: "))
    if(a>n):
        print("Too high!")
        guesses += 1
    elif(a<n):
        print("Too low!")
        guesses += 1

print("You guessed it in", guesses, "tries!")        