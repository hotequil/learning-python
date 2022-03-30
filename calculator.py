print("Calculator")

first_number = float(input("First number: "))
second_number = float(input("Second number: "))
operation = int(input("Choose an operation (1 - Addition | 2 - Subtraction | 3 - Multiplication | 4 - Division): "))
result = 0

if operation == 1:
    result = first_number + second_number
elif operation == 2:
    result = first_number - second_number
elif operation == 3:
    result = first_number * second_number
else:
    result = first_number / second_number

print("Result is {:.2f}".format(result))
