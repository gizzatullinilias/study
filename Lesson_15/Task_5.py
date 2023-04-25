from time import sleep

class TrafficLight:
    def __init__(self, color):
        self._color = color
    def running(self):
        for key, value in self._color.items():
            sleep(value)
            print(key)


traf = TrafficLight(color={
    "Красный": 1,
    "Желтый": 0.5,
    "Зеленый": 2})
traf.running()