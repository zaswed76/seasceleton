from enum import Enum

class CellStatus(Enum):
    empty = "0"
    deck = "#"
    killed = "X"


class Cell:

    def __init__(self, x, y):
        self.__y = y
        self.__x = x
        self.coord = (self.__x, self.__y)
        self.status = CellStatus.empty

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __repr__(self):
        return "C{}".format(self.status.value)
