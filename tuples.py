categories = ("standard", "premium", "deluxe")
print("declaration: {}".format(categories))

index_one = categories[1]
print("index 1: {}".format(index_one))

last_index = categories[-1]
print("last index: {}".format(last_index))

position_zero, position_one, position_two = categories
print("position zero: {} | position one: {} | position two: {}".format(position_zero, position_one, position_two))

for category in categories:
    print("category: {}".format(category))
