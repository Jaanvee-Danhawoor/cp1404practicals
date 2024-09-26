total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(1, number_of_items + 1):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item
if total_price > 100:
    total_price = 0.9 * total_price  # 10% discount
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
