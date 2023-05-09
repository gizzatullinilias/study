class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def __str__(self):
        return '->'.join(str(i) for i in self.items)

    def add_center(self, item):
        middle = len(self.items) // 2
        self.items.insert(middle, item)

    def remove_center(self):
        middle = len(self.items) // 2
        return self.items.pop(middle)


q = Deque()
q.add_front("лоп")
q.add_rear("Bob")
q.add_center("прога")

print(q)
q.remove_front()
print(q)
q.remove_rear()
print(q)

q.add_front("яблоко")
print(q)
q.add_rear("Рома")
print(q)
q.remove_center()
print(q)
