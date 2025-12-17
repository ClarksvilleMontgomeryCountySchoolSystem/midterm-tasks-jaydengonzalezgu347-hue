#Given variables
party_pizza_mini = 14
large = 8
medium = 6
people = 6 # friends

#Do Not use crtl+A to select code.  Only copy the code below this line.
#------------------------------------------------------------------------------------------------
total_slices = large + medium + party_pizza_mini
print(f" Total number of slices: {total_slices}")

people += 1
share = total_slices // people
leftover = total_slices % people
print(f"Each person gets {share}")
print(f"Leftover: {leftover}")

people += 2
share = total_slices // people
leftover = total_slices % people
print(f"Each person gets {share}")
print(f"Leftover: {leftover}")

#Mom says "Wait, Brandon’s coming. We’re going to need more pizza. I’ll upgrade the mini to a party_pizza instead. It’s the same as 2 minis. Hopefully the leftovers will be enough to fill his hollow leg.”

total_slices += party_pizza_mini
share = total_slices // people
leftover = total_slices % people
print(f"Each person gets {share}")
print(f"Leftover: {leftover}")
print("...for Mr. Hollow Leg")
