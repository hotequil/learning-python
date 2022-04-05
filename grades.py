grades = []
option = None

while option != 4:
    option = int(input("Select an option: \n1) Add a grade \n2) See grades \n3) Calculate media \n4) Exit \n"))

    if option == 1:
        grades.append(float(input("Digit a grade: \n")))

        print("Added with success! \n")
    elif option == 2:
        for index in range(len(grades)):
            print("Grade ({}): {:.2f} \n".format(index + 1, grades[index]))
    elif option == 3:
        media = 0
        length = len(grades)

        for index in range(length):
            media += grades[index]

        media /= length

        print("Media: {:.2f}".format(media))

print("Thanks! See you later")
