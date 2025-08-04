a = int(input("Enter your age: "))

if(a%2 == 0):
    print("a is even")

else:
    print("a is odd")    

if(a>=18):
    print("You are above the age of consent")

elif(a<0):
    print("You are entering an invalid age")

else:
    print("You are below the of consent")

print("End of program")        