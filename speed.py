distance = input("Distance: ")
time = input("Time: ")
media_speed = float(distance) / float(time)
phrase = "Speed is {:.2f}km/h".format(media_speed)

print(phrase)
