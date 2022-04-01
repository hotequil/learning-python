points = float(input("Digit your points: "))

if points >= 1000:
    print("You earned 3gb for free")
elif points >= 500:
    print("You earned 1.5gb for free")
elif points >= 200:
    print("You earned 500mb for free")
else:
    print("You earned nothing")
