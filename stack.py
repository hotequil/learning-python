class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        return str(self.list)

    def add(self, item):
        self.list.append(item)

    def remove(self):
        return self.list.pop()

    def is_empty(self):
        return not self.list

stack = Stack()

stack.add(1)
stack.add(2)
stack.add(3)
stack.add(4)

print(f"remove: {stack.remove()}")
print(f"is_empty: {stack.is_empty()}")
print(f"str stack: {str(stack)}")
