class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        result = ''
        for row in self.data:
            result += '| ' + ' | '.join(str(i) for i in row) + ' |\n'
        return result


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m)


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        result = ''
        for row in self.data:
            result += '| ' + ' | '.join(str(i) for i in row) + ' |\n'
        return result

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError('Matrix sizes must be equal')
        result = []
        for i, row in enumerate(self.data):
            new_row = []
            for j, elem in enumerate(row):
                new_row.append(elem + other.data[i][j])
            result.append(new_row)
        return Matrix(result)


m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
m3 = m1 + m2
print(m1)
print(m2)
print(m3)
