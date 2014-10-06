#Paul Njenje
#06/10/2014
#Selection class exercise Revision 4

number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter a different number: "))
number3 = int(input("Please enter a third number: "))
              
if number1 > number2 and number2 > number3:
    print("{0} is greater than {1}".format(number1, number2))
elif number3 > number1 and number2 < number1:
    print("{0} is greater than {1}".format(number3, number1))
elif number1 == number2:
    print("These numbers are the same")
else:
    print("{0} is greater than {1}".format(number2, number1))
