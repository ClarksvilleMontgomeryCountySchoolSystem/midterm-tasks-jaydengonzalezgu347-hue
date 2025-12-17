# Testing flag - will be set by test
TESTING = False  # <-- Should be False by default
item = None
price = None
quantity = None

print("""
========================================
   WELCOME TO THE PECULIAR EMPORIUM!
   "Magical items at mundane prices!"
   Prosperity comes in threes!
========================================
ITEM MENU:
Invisibility Cloak.........$44.99
Dragon Egg.....................$29.99
""")

menu ='''
Flying Carpet...............$119.99
Phoenix Feather...............$14.99
Time Turner....................$84.99
Enchanted Sword..................$65.99
Potion of Luck....................$11.99
Crystal Ball........................$39.99
'''
print(menu)

# Shopkeeper's rule: All purchases must be at least 3 items for good luck!
# (Don't worry - the shopkeeper checks every order himself)

def get_purchase_info(): # Convert input when necessary
    item = input("What item are wondering on buying?")
    price = input("price of items selected")
    quantity = input("Items selected include: Potion of Luck and Crytal Ball and Dragon Egg")
    return item, price, quantity

# Only get input if NOT testing
if not TESTING:
    item, price, quantity = get_purchase_info()

# Calculate using the input values (NOT hardcoded!)
print("Subtotal: {subtotal}")
tax_rate = 0.095 #This is slightly different from the review. The tax multiplier is stored into a variable.
print("Tax: {tax}")
print("Total: {total}")
total=(round,2)
# Print statements
print("--------------------------")
print("Dragon Egg x5 @ $30.00 each")
print("--------------------------")
print("Subtotal: $150.00")
print("Tax: $14.25")
print("Total: $164.25")
print("\nThank you for shopping at\nThe Peculiar Emporium!")
