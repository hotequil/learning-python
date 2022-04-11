class Queue:
    def __init__(self):
        self.list = []

    def __str__(self):
        return str(self.list)

    def add(self, item):
        self.list.append(item)

    def remove(self):
        return self.list.pop(0)

    def is_empty(self):
        return not self.list

queue = Queue()

queue.add(1)
queue.add(2)
queue.add(3)
queue.add(4)

print(f"remove: {queue.remove()}")
print(f"is_empty: {queue.is_empty()}")
print(f"str queue: {queue}")
