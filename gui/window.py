from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QGridLayout,  QTabWidget

from gui.tab1 import addTab1
from gui.tab2 import addTab2
from gui.tab3 import addTab3


class mainWindow(QTabWidget):
    def __init__(self):
        super().__init__()

        self.title = "ER Calculator"
        self.left = 50
        self.top = 50
        self.width = 800
        self.height = 600
        self.icon = "images/Credit.png"
        self.create_ui()

        addTab1(self)
        addTab2(self)
        addTab3(self)

    def create_ui(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.icon))
        self.setStyleSheet("""
            """)