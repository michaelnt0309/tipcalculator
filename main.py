bill = float(input("What is the bill amount? "))
people = int(input("How many people are splitting the bill? "))
tip = float(input("What is the tip amount? "))
cost = (bill / people) * tip
final_cost = "{:.2f}".format(cost)
print(f"Each person needs to pay ${final_cost} dollars")
