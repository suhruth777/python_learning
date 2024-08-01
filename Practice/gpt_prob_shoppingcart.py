# Create a program that calculates the total cost of items in a shopping cart. The program should:
# 1. Ask the user how many items they want to input.
# 2. Use a loop to get the name and price of each item from the user and store them in a dictionary.
# 3. Calculate the total cost.
# 4. Print the total cost and list each item with its price.

num_items = int(input("Enter how many items you would like in your cart: "))
shopping_cart = {}

for i in range(num_items):
    item_name = input('Enter item name: ')
    item_price = float(input('Enter item price: '))
    shopping_cart.update({item_name:item_price})

total_cost = sum(shopping_cart.values())
print(f'Your total cost is: ${total_cost:.2f}')

print("Here's your reciept: ")
for key, value in shopping_cart.items():
    print(f'{key}: ${value:.2f}')


