from datetime import time

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self._time = time(hours, minutes, seconds)

    @classmethod
    def from_string(cls, time_str):
        hours, minutes, seconds = map(int, time_str.split(":"))
        return cls(hours, minutes, seconds)

    def __str__(self):
        return str(self._time)

time_str = "23:59:59"
time = Time.from_string(time_str)
print(time)
