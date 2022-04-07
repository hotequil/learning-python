file = open("./text.txt", encoding="UTF-8")

print(f"file: {file}")
print(f"read: {file.read()}")

file.close()

new_file = open("./new-file.txt", "w", encoding="UTF-8")

new_file.write("hello world")
new_file.close()
