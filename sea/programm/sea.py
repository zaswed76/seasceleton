
from collections.abc import Sequence, Collection
import numpy as np

from cell import Cell, CellStatus
from ship import Ship

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






if __name__ == '__main__':
    sea = Sea(5, 5)
    ship = Ship(Cell(1, 1), Cell(1, 2))
    print(ship)

