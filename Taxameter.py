start_price = 3.2
km = int(input("Bitte Kilometer eingeben: "))
if km > 5:
    costs = 1.9
else:
    costs = 2.1
total_expenses = start_price + km * costs
print("Deine Kosten sind:", total_expenses,"€")
