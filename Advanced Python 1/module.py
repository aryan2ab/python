def myFunc():
    print("Hello World")

myFunc()    
print(__name__)

if __name__ == "__main__":
    # If this code is directly executed by the running the file its present in
    print("We are directly running this code")
    myFunc()
    print(__name__)