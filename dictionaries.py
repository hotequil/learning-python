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
