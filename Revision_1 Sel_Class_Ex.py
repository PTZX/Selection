#Paul Njenje
#selection class Ex Rev 1
#01-10-14

number = int(input("Please enter a number: "))
number1 = int(input("Please enter a second number: "))

print("You chose {0} and {1}".format(number, number1))

if number == number1:
    print("These numbers are the same, Well done!")
elif number != number1:
    print("Try and enter a matching pair of numbers.")
