# Task 1 code correction
number = int(input("Enter a number: ")) #added int() to input. Can't calculate a string.

if number > 0:
    print("The number is positive.")
elif number == 0: # added an = sign to make the condition (is equal ==) instead of a variable (number = 0).
    print("The number is zero.")
else: # removed the condition from the else statement. 
    print("The number is negative.")