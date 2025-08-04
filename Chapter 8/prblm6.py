def inch_to_cm(inch):
    return inch * 2.54

n = int(input("Enter your number in inches: "))
print(f"The corresponding value in centimeters is: {inch_to_cm(n)} cm")