from sortedcontainers import SortedList


class DataStream:
    def __init__(self):
        self.sl = SortedList()

    def add_value(self, value):
        self.sl.add(value)


