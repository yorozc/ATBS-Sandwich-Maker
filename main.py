import pyinputplus as pyip

prices = {'bread': {'wheat': 2, 'white': 3, 'sourdough': 5},
          'protein': {'chicken': 12, 'turkey': 15, 'ham': 10, 'tofu': 5},
          'cheese': {'cheddar': 2, 'swiss': 3, 'mozzarella': 1}}


print("Choose sandwich components.")
print("===========================")
bread = pyip.inputMenu(list(prices['bread']))
print(f"{bread.capitalize()} bread has been chosen.")
print("===========================")
protein = pyip.inputMenu(list(prices['protein']))
print(f"{protein.capitalize()} has been chosen.")
print("===========================")