correct_surname = "hotequil"
surname = None

while surname != correct_surname:
    if surname is not None:
        print("You are wrong!")

    surname = input("What's my surname? ")

print("Congratulations, you are right!")
