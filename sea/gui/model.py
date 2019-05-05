
from PyQt5.QtCore import *

class Model:
    def __init__(self):
        self._x = 0

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, v):
        self._x = v

    def up_x(self):
        print("model up_x")
        self.x += 2

class Adapter(QObject, Model):
    def __init__(self):
        super().__init__()

    def up_x(self):
        print("adapter up_x")
        super().up_x()
        self.x += 2

if __name__ == '__main__':
    adp = Adapter()
    adp.up_x()
    print(adp.x)