from PyQt6.QtWidgets import QFormLayout, QLineEdit, QWidget


def addTab1(self):
    self.tab1 = QWidget()
    self.addTab(self.tab1, "Tab 1")
    self.tab1.setStyleSheet("""
    """)

    layout = QFormLayout()
    layout.addRow("Name", QLineEdit())
    layout.addRow("Example", QLineEdit())
    self.setTabText(0, "Main")
    self.tab1.setLayout(layout)
