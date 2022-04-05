def get_grade_media():
    first_grade = float(input("Digit your first grade: "))
    second_grade = float(input("Digit your second grade: "))
    media = (first_grade + second_grade) / 2

    return "{:.2f}".format(media)


print("Your media is {}".format(get_grade_media()))
