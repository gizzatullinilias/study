class Queue:
    def __init__(self):
        self.inside = []

    def add(self, name):
        self.inside.append(name)

    def take_out(self):
        if len(self.inside) > 0:
            self.inside.pop(0)

    def __str__(self):
        return "=>".join(self.inside)

    def __add__(self, name):
        self.add(name)
        return self

    def __sub__(self, name):
        self.take_out()
        return self

    def __iadd__(self, name):
        self.add(name)
        return self

    def __isub__(self, name):
        self.take_out()
        return self


q = Queue()
q.add("Alice")
q.add("Bob")
q.add("Cindy")

print(q)

q.take_out()
print(q)

q1 = q + "David"
print(q1)

q1 -= "Bob"
print(q1)
