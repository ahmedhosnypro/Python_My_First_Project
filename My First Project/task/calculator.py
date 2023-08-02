# income
bubblegum = 202
toffee = 118
ice_cream = 2250
milk_chocolate = 1680
doughnut = 1075
pancake = 80

print("Earned amount:")
print("Bubblegum: $", bubblegum)
print("Toffee: $", toffee)
print("Ice cream: $", ice_cream)
print("Milk chocolate: $", milk_chocolate)
print("Doughnut: $", doughnut)
print("Pancake: $", pancake)
print()
print("Income: $", bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake)
print("Staff expenses:")
staff_expenses = int(input())

print("Other expenses:")
other_expenses = int(input())

print("Net Income: $", bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake
      - staff_expenses - other_expenses)
