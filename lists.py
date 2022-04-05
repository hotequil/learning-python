fruits = ["apple", "banana", "strawberry", "strawberry", "strawberry", "strawberry", "strawberry"]
print("declaration: {}".format(fruits))

fruits.append("pineapple")
fruits.append(input("Put a new fruit: "))
print("append: {}".format(fruits))

fruits.insert(2, "blueberry")
print("insert: {}".format(fruits))

fruits.pop()
print("pop: {}".format(fruits))

fruits.pop(5)
print("pop index 5: {}".format(fruits))

fruits.remove("banana")
print("remove: {}".format(fruits))

print("length: {}".format(len(fruits)))

print("count of strawberry: {}".format(fruits.count("strawberry")))

fruits.sort()
print("sort: {}".format(fruits))

fruits.reverse()
print("reverse: {}".format(fruits))
