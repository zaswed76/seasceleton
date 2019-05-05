from PyQt5.QtCore import QObject


class Controller(QObject):
    def __init__(self, model):
        super().__init__()
        self.model = model

    def up_value(self):
        self.model.up_value()

    def down_value(self):
        self.model.down_value()