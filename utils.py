def get_grade_media():
    first_grade = float(input("Digit your first grade: "))
    second_grade = float(input("Digit your second grade: "))
    media = (first_grade + second_grade) / 2

    return "{:.2f}".format(media)


print("Your media is {}".format(get_grade_media()))


def which_is_the_biggest(first_number, second_number):
    temporary = None

    if first_number > second_number:
        temporary = first_number
    elif first_number < second_number:
        temporary = second_number

    return temporary


print("Biggest is {}".format(which_is_the_biggest(5, 10)))
print("Biggest is {}".format(which_is_the_biggest(8, 2)))
print("Biggest is {}".format(which_is_the_biggest(6, 6)))
