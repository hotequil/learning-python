fruits = ["apple", "banana", "strawberry", "strawberry", "strawberry", "strawberry", "strawberry"]

print(fruits)

fruits.append("pineapple")
fruits.append(input("Put a new fruit: "))
fruits.insert(2, "blueberry")

print(fruits)

fruits.pop()

print(fruits)

fruits.remove("banana")

print(fruits)
print(len(fruits))
print(fruits.count("strawberry"))
