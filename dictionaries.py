products = {
    "shelf_one": "beer",
    "shelf_two": "coffee",
    "shelf_three": "water",
    "shelf_four": "banana"
}

products_values = products.values()
products_keys = products.keys()
items = products.items()

print(f"declaration: {products}")
print(f"type: {type(products)}")
print(f"values: {products_values}")
print(f"keys: {products_keys}")
print(f"shelf two: {products['shelf_two']}")
print(f"items: {items}")

for product in products_values:
    print(f"product: {product}")

for key in products_keys:
    print(f"key: {key}")

for product_key, product_value in items:
    print(f"key: {product_key} | value: {product_value}")

products["shelf_four"] = "tomato"
products["shelf_five"] = "car"

print(f"shelf four: {products['shelf_four']}")
print(f"shelf five: {products['shelf_five']}")
print(f"products: {products}")

shelf_key = input("Put a shelf: ")
product_name = input("Put a product: ")
products[shelf_key] = product_name

print(f"{shelf_key}: {product_name}")
print(f"products: {products}")

products.pop("shelf_two")

print(f"products: {products}")

products.popitem()

print(f"products: {products}")

contacts = {
    "hotequil": {
        "email": "hotequil@email.com",
        "phone": 1234
    },
    "joao": {
        "email": "joao@email.com",
        "phone": 5678
    }
}

print(f"contacts: {contacts}")
