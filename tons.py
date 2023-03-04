#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces
input = input()
Tons = int(float(input) / 32000)
Tons_remain = float(input) % 32000
Pounds = int(float(Tons_remain) / 16)
Pounds_remain = float(input) % 16
Ounces = int(float(Pounds_remain))

print(("Tons: ") + str(Tons))
print(("Pounds: ") + str(Pounds))
print(("Ounces: ") + str(Ounces))
