from abc import ABC, abstractmethod
class Stationery(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def draw(self):
        pass

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.color = 'blue'

    def draw(self):
        print(f'Ручка {self.title} пишет цветом {self.color}')

class Pencil(Stationery):
    def draw(self):
        print(f'Карандаш {self.title} рисует серыми линиями')

class Handle(Stationery):
    def draw(self):
        print(f'Маркер {self.title} выделяет текст ярко-оранжевым цветом')


pen = Pen('широкая')
pen.draw()

pencil = Pencil('простой')
pencil.draw()
handle = Handle('толстый')
handle.draw()


class Stationery(ABC):
    color = None

    @classmethod
    def set_color(cls, color):
        cls.color = color

Stationery.set_color('yellow')
print(Pen.color)
print(Pencil.color)
print(Handle.color)
