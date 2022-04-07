file = open("./text.txt", encoding="UTF-8")

print(f"file: {file}")
print(f"read: {file.read()}")

file.close()
