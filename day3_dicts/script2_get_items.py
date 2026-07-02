# Script 2 — get() and items():
# Given a dictionary of product prices, use .get() to safely check a product that may not exist. Loop through using .items() and print formatted output.

products = {
    "Laptop": 50000,
    "Mobile": 25000,
    "Tablet": 18000,
    "Mouse": 700,
    "Keyboard": 1200
}

# Safely check a product
price = products.get("Charger","Product Not Found")
print(price)

print("Product List:")
for product, price in products.items():
    print(product,":",price)