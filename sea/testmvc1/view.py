from PyQt5 import QtWidgets


class View(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(500, 200)
        box = QtWidgets.QHBoxLayout(self)
        self.btn_up = QtWidgets.QPushButton("up")
        self.btn_down = QtWidgets.QPushButton("down")
        self.lb = QtWidgets.QLabel()

        box.addWidget(self.btn_up)
        box.addWidget(self.lb)
        box.addWidget(self.btn_down)