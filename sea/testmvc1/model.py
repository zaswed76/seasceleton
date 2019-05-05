from PyQt5.QtCore import *


class Model(QObject):
    value_changed = pyqtSignal(int)
    color_changed = pyqtSignal(str)
    up_block_signal = pyqtSignal(bool)
    down_block_signal = pyqtSignal(bool)


    def __init__(self):
        super().__init__()
        self.__value = 0
        self.__current_lb_color = "grey"
        self.__up_block = False
        self.__down_block = False
        self.top_limit = 10
        self.down_limit = 0

    @property
    def down_block(self):
        return self.__down_block

    @down_block.setter
    def down_block(self, b):
        self.__down_block = b
        self.down_block_signal.emit(b)

    @property
    def up_block(self):
        return self.__up_block

    @up_block.setter
    def up_block(self, b):
        self.__up_block = b
        self.up_block_signal.emit(b)

    @property
    def current_lb_color(self):
        return self.__current_lb_color

    @current_lb_color.setter
    def current_lb_color(self, color):
        self.__current_lb_color = color
        self.color_changed.emit(color)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
        self.value_changed.emit(value)

    def up_value(self):
        self.value += 1
        if self.value > 5:
            self.current_lb_color = "white"
        if self.value >= self.top_limit:
            self.up_block = True
        else:
            self.up_block = False
        if self.value > self.down_limit:
            self.down_block = False

    def down_value(self):
        self.value -= 1
        if self.value <= 5:
            self.current_lb_color = "grey"
        if self.value <= self.down_limit:
            self.down_block = True
        else:
            self.down_block = False
        if self.value < self.top_limit:
            self.up_block = False

if __name__ == '__main__':
    adapter = Model()
    adapter.up_value()
    print(adapter.value)