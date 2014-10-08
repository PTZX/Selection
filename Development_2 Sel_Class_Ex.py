#Paul Njenje
#08/10/2014
#Selection Class Exercise Dev 2

print("This program will display the state of water at the temperature you choose.")

temperature = int(input("Enter a temperature in degrees centigrade: "))

if temperature <= 0:
    print("Water will be Frozen at the is temperature.")
elif temperature <= 99:
    print("Water is neither frozen or boiling at this temperature.")
else:
    print("Water will Boil at this temperature.")
    
