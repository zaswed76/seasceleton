
from collections.abc import Sequence, Collection
import numpy as np
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

class Sea(Sequence):
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.__matrix = []
        self.create_matrix()

    def set_ship(self, ship):
        for cell in ship:
            self(cell).status = CellStatus.deck

    def create_matrix(self):
        self.__matrix.clear()
        _range = range(self.height)
        for y in _range:
            self.__matrix.append([Cell(y, x) for x in range(self.width)])

    def __contains__(self, value):
        for i in self.__matrix:
            for x in i:
                print(type(x))
                if value == x.coord:
                    return True
            else:
                return False

    def __repr__(self):
        return str(np.array(self.__matrix))

    def __call__(self, cell):
        return self.__matrix[cell[0]][cell[1]]

    def __getitem__(self, item):
         return self.__matrix[item]

    def __len__(self):
        return None

    def check_cell(self, p):
        return self(p).status


class Ship(Collection):
    NotfoundStat = 0
    WondStat = 1
    killStat = 2
    def __init__(self, *cells):
        self.decks = cells
        self.__status = Ship.NotfoundStat

    @property
    def status(self):
        return self.__status


    def check_status(self):
        return self.decks

    def __repr__(self):
        return str(self.decks)

    def __getitem__(self, item):
         return self.decks[item]

    def __len__(self):
        return len(self.decks)

    def __iter__(self):
        return iter(self.decks)

    def __contains__(self, value):
        return value in self.decks



if __name__ == '__main__':
    sea = Sea(5, 5)
    ship = Ship(Cell(1, 1), Cell(1, 2))
    print(ship)

