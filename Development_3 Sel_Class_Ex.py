#Paul Njenje
#10/10/14
#Selection Class Statements Dev 3

print("This program will calculate your gross pay.")

hours = int(input("Enter the hours you work in a week: "))
rate = float(input("Enter your hourly rate: £"))

if hours > 40:
    rate = rate * 1.5

pay = hours * rate



if hours < 1 and hours > 60:
    print("These hours are not in range")
else: print("£{0} a week".format(pay))
