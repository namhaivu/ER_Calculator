import sys

from PyQt6.QtWidgets import QApplication

from examples.example import example1
from gui.window import mainWindow

if __name__ == '__main__':
    example1()
    app = QApplication(sys.argv)
    Window = mainWindow()
    Window.show()
    sys.exit(app.exec())