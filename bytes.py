import sys

name = "hotequil"
list = []
tuple = ()

print("name bytes: {}".format(sys.getsizeof(name)))
print("list bytes: {}".format(sys.getsizeof(list)))
print("tuple bytes: {}".format(sys.getsizeof(tuple)))
