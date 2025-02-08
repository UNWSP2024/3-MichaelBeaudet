# Author: Michael Beaudet
# Title: Week 3 Program 5
# Date 2/7/25

def cost_calculation():
    hot_dog_cost = 3.50
    chili_dog_cost = 4.50 
    cheese_cost = 0.50
    peppers_cost = 0.75
    grilled_onions_cost = 1.00 
    tax_rate = 0.07
# Get hot dog choice
    print("Choose what hot dog you want: ")
    print("Hot Dog: $3.50")
    print("Chili Dog: $4.50")
    choice = input('Enter "Regular" for a normal hot dog or "Chili" for a chili dog: ')
# Get the hot dog type and price
    if choice == "Regular":
        base_price = hot_dog_cost
    elif choice == "Chili":
        base_price = chili_dog_cost
    else:
        print("Invalid choice")
        return
# Ask if they want toppings
    cheese = input("Do you want cheese? ($0.50) (yes or no): ")
    peppers = input("Do you want peppers? ($0.75) (yes or no): ")
    onions = input("Do you want onions? ($1.00) (yes or no): ")
# Add the price of the toppings to the base price
    total_price = base_price
    if cheese == "yes":
        total_price += cheese_cost
    if peppers == "yes":
        total_price += peppers_cost
    if onions == "yes":
        total_price += grilled_onions_cost
# Calculate tax and total cost
    tax = total_price * tax_rate
    total = total_price + tax
# Display total
    print(f"Total Cost: ${total:.2f}")

cost_calculation()
