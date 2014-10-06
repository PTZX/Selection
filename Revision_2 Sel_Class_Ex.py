#Paul Njenje
#06/10/2014
#Selection class exercise Revision 2

print("Please enter your age to find out if your old enough to drive.")

age = int(input("Enter your age here: "))

if age >= 17:
    print("You are old enough to drive")
elif age < 17 and age > 0:
    print ("You are too young to drive")
else:
    print("Enter an age over 0")
