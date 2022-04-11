class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

    def set_next(self, next_node):
        self.next = next_node

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value

first_node = Node(10)
second_node = Node(20)

print(f"first_node: {first_node}")
print(f"type: {type(first_node)}")
print(f"get_next: {first_node.get_next()}")
print(f"get_value: {first_node.get_value()}")

first_node.set_next(second_node)

print(f"get_next: {first_node.get_next()}")
