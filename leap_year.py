<<<<<<< HEAD
year = int(input("Enter a year: "))

if year % 400 == 0 and year % 100 == 0:
    print("Leap year.")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year.")
else:
=======
year = int(input("Enter a year: "))

if year % 400 == 0 and year % 100 == 0:
    print("Leap year.")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year.")
else:
>>>>>>> c1cf3ab1c5ea38fffee7ace798d39ecc813f1d0f
    print("Not a leap year.")