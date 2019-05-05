import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication

from sea.testmvc1 import model, controller
from sea.testmvc1 import main as _main


def qt_message_handler(mode, context, message):
    if mode == QtInfoMsg:
        mode = 'INFO'
    elif mode == QtWarningMsg:
        mode = 'WARNING'
    elif mode == QtCriticalMsg:
        mode = 'CRITICAL'
    elif mode == QtFatalMsg:
        mode = 'FATAL'
    else:
        mode = 'DEBUG'
    print('qt_message_handler: line: %d, func: %s(), file: %s' % (
          context.line, context.function, context.file))
    print('  %s: %s\n' % (mode, message))
qInstallMessageHandler(qt_message_handler)

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = model.Model()

        self.controller = controller.Controller(self.model)

        self.main = _main.Main(self.model, self.controller)
        self.model.value = 1
        self.main.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())
