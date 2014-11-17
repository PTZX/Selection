#Paul Njenje
#13/10/14
#Selection Statemant Spot check Q1

print("This program will check to see if your attendance is at the required level")

attendPercentage = int(input("Please enter your Attendance percentage: "))
requiredPercentage = 85

if attendPercentage <= requiredPercentage and attendPercentage > 0:
    print("Your attendance is only {0}%. You must improve your attendance.".format(attendPercentage))
elif attendPercentage > requiredPercentage and attendPercentage < 100:
    print("Your attendance is {0}%. Keep up the good attendance.".format(attendPercentage))

else:
    print("This is an invalid attendance percentage. Please enter your percentage as a whole number and without a percentage sign.")
