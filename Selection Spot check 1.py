#Selection Spot Check Q2

firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")
gender = input("Please enter your gender (M/F): ")

if gender == ("M"):
    print("Mr {0} {1}".format(firstName, lastName))
elif gender == ("F"):
    print("Ms {0} {1}".format(firstName, lastName))
else:
    print("Please enter an appropriate gender.")
