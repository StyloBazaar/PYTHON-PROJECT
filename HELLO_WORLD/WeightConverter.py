import math
weight = float(input("Weight : "))
unit = input("(L)bs or (K)gs ? ")
if unit == 'L' or unit == 'l':
    kg = round(weight*0.453592)
    print(f"{kg} kgs")
elif unit == 'K' or unit == 'k':
    lb = round(weight * 2.2042)
    print(f"{lb} lbs")
else:
    print("Please enter your weight unit. L for Lbs. K for Kgs.")