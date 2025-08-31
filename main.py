import pyinputplus as pyip

prices = {'bread': {'wheat': 2, 'white': 3, 'sourdough': 5},
          'protein': {'chicken': 12, 'turkey': 15, 'ham': 10, 'tofu': 5},
          'cheese': {'cheddar': 2, 'swiss': 3, 'mozzarella': 1},
          'condiments': {'mayo': 0.25, 'mustard': 0.30},
          'veggies': {'lettuce': 0.10, 'tomato': 0.25}}

cost = 0

print("Choose sandwich components.")

print("===========================")
bread = pyip.inputMenu(list(prices['bread']))
print(f"{bread.capitalize()} bread has been chosen.")
cost += prices['bread'][bread]
print("===========================")

protein = pyip.inputMenu(list(prices['protein']))
print(f"{protein.capitalize()} has been chosen.")
cost += prices['protein'][protein]
print("===========================")

cheeseChoice = pyip.inputYesNo(prompt="Would you like cheese?\n:")
if cheeseChoice == "yes":
    print("===========================")
    cheese = pyip.inputMenu(list(prices['cheese']))
    print(f"{cheese.capitalize()} has been chosen.")
    cost += prices['cheese'][cheese]
else:
    print("===========================")
    print("No cheese")
print("===========================")

mayo = pyip.inputYesNo(prompt="Would you like mayo?\n:")
if mayo == "yes":
    print("===========================")
    print("Mayo has been added.")
    cost += prices['condiments']['mayo']
print("===========================")


mustard = pyip.inputYesNo(prompt="Would you like mustard?\n:")
if mustard == "yes":
    print("===========================")
    print("Mustard has been added.")
    cost += prices['condiments']['mustard']
print("===========================")


lettuce = pyip.inputYesNo(prompt="Would you like lettuce?\n:")
if lettuce == "yes":
    print("===========================")
    print("lettuce has been added.")
    cost += prices['veggies']['lettuce']
print("===========================")


tomato = pyip.inputYesNo(prompt="Would you like tomato?\n:")
if tomato == "yes":
    print("===========================")
    print("tomato has been added.")
    cost += prices['veggies']['tomato']
print("===========================")

amount = pyip.inputInt(prompt="How many sandwiches would you like?\n:", min=1)

cost *= amount

print(f"Total cost: {cost:.2f}")