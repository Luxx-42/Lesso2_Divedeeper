# Task 1 identify the geatest

enter_3_numbers = input("Enter 3 numbers, but first enter ok: ")
first_number = int(input("first number: "))
second_number = int(input("Second number: "))
third_number = int(input("Third number: "))

if enter_3_numbers and first_number and second_number and third_number:
    min_number = min(first_number, second_number, third_number)
    max_number = max(first_number, second_number, third_number)

print(f"The smallest number is {min_number}. The largest number is {max_number}") 
