def main():
    try:
        a = int(input("hey, enter a number: "))

        print(a)

 
    except Exception as e:
        print(e)

    finally:
        print("i am inside finally")    

main()
