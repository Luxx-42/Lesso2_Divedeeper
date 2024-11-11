years = int(input("Enter a year, example (1984): "))

if years % 400 == 0:
    print("this is a leap year")   
elif years % 100 == 0:
    print("this is not a leap year")    
elif years % 4 == 0:
    print("this is a leap year")
else:
    print("This is not leap year")