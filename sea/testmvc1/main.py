from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

from sea.testmvc1 import view


class Main(QtWidgets.QWidget):
    def __init__(self, model, controller, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.controller = controller
        self.model = model

        self.model.value_changed.connect(self.on_value_changed)
        self.model.color_changed.connect(self.on_color_changed)
        self.model.up_block_signal.connect(self.up_block_changed)
        self.model.down_block_signal.connect(self.down_block_changed)
        self.base = view.View(self)
        self.base.btn_up.clicked.connect(self.controller.up_value)
        self.base.btn_down.clicked.connect(self.controller.down_value)

    @pyqtSlot(int)
    def on_value_changed(self, v):
        self.base.lb.setText(str(v))

    def on_color_changed(self, color):
        self.setStyleSheet("background-color: {}".format(color))

    def up_block_changed(self, b):
        self.base.btn_up.setDisabled(b)

    def down_block_changed(self, b):
        self.base.btn_down.setDisabled(b)