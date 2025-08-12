#Using walrus operator to assign a value to a variable while also using it in an expression

if (n:= len([1, 2, 3, 4, 5])) > 3:
    print(f"List has {n} elements, which is more than 3.")