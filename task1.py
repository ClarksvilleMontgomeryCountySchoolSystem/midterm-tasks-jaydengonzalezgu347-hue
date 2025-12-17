slices = large + medium + party_pizza_mini
print(f" Total number of slices: {slices}")

people += 1
share = slices // people
leftover = total_slices % people
print(f"Each person gets {share}")
print(f"Leftover: {leftover}")

people += 2
share = slices // people
leftover = slices % people
print(f"Each person gets {share}")
print(f"Leftover: {leftover}")

#Mom says "Wait, Brandon’s coming. We’re going to need more pizza. I’ll upgrade the mini to a party_pizza instead. It’s the same as 2 minis. Hopefully the leftovers will be enough to fill his hollow leg.”

slices += party_pizza_mini
share = slices // people
leftover = slices % people
print(f"Each person gets {share}")
print(f"Leftover: {leftover}")
print("...for Mr. Hollow Leg")
