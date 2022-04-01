print("Programming course")

name = input("Digit your name: ")
age = int(input("Digit your age: "))

if age >= 18:
    print("You're registered in our course, {}! Because you're {} years old".format(name, age))
else:
    can = input("You aren't of age, {}, you are {} years old. We need your parents permission. Do they agree (yes or no): ".format(name, age))

    if can == "yes":
        print("You're registered, {}!".format(name))
    else:
        print("You aren't registered, {}!".format(name))
