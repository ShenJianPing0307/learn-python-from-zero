data = [
    {"name": "apple", "price": 6, "quantity": 100},
    {"name": "pear", "price": 8.5, "quantity": 230},
    {"name": "banana", "price": 6, "quantity": 150},
]

# price + 1
# price average

total_price = 0
for item in data:
    item["price"] = item.get("price") + 1
    total_price += item.get("price")

avr = total_price / len(data)
print(data)
print(avr)
