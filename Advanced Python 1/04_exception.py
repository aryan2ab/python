try:
    a = int(input("hey, enter a number: "))

    print(a)

except ValueError as v:
    print("hEYYY")
    print(v)
except Exception as e:
    print(e)

print("thank you")        