class Battery:
    def __init__(self, initial_capacity=[], max_charge=5):
        self.capacity = initial_capacity
        self.max_charge = max_charge

    def charge(self):
        if len(self.capacity) < self.max_charge:
            self.capacity.append(')')

    def discharge(self):
        if len(self.capacity) > 0:
            self.capacity.pop()

    def __str__(self):
        return '[' + ''.join(self.capacity) + ']'


print("Initializing Battery...")
b = Battery()
print(b)

print("Charging Battery...")
b.charge()
print(b)

print("Discharging Battery...")
b.discharge()
print(b)
