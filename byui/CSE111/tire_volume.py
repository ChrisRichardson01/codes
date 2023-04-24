import math
import datetime

pi = math.pi

w = int(input("Enter the width of the tire in mm (ex. 205): "))
a = int(input("Enter the aspect ratio of the tire (ex. 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex. 15): "))

print(f"The tire you entered is a {w}/{a}R{d}")
v = (pi * (pow(w, 2) * a * (w * a + 2540 * d))) / 10000000000
print("The volume of that tire is %.2f liters" % v)

# Finding tire prices online
if w == 205 and a == 60 and d == 15:
    print("Price of the tire is $100")
elif w == 195 and a == 55 and d == 16:
    print("Price of the tire is $120")
elif w == 225 and a == 50 and d == 17:
    print("Price of the tire is $150")
else:
    print("Price not found")

# Store phone number if user wants to buy tires
buy = input("Do you want to buy tires with these dimensions? (yes or no): ")
if buy.lower() == "yes" or buy.lower() == "y":
    phone = input("Please enter your phone number: ")
    today = datetime.date.today().strftime("%m/%d/%Y")
    with open("volumes.txt", "a") as f:
        f.write(f"{today},{w},{a},{d},{v},{phone}\n")
        print("Phone number stored in volumes.txt")
else:
    print("Thank you for using our tire volume calculator!")