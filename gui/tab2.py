from PyQt6.QtWidgets import QWidget, QComboBox, QGridLayout, QRadioButton, QLineEdit, QLabel


def addTab2(self):
    self.tab2 = QWidget()
    self.addTab(self.tab2, "Tab 2")
    self.tab1.setStyleSheet("""
    """)
    layout = QGridLayout()

    character_picker = QComboBox()
    character_picker.addItem('Abigail')
    character_picker.addItem('Adela')
    character_picker.addItem('Adina')
    character_picker.addItem('Adriana')
    layout.addWidget(character_picker, 0 ,0, 1, 2)

    layout.addWidget(QRadioButton("option1"), 1, 0, 1, 1)
    layout.addWidget(QRadioButton("option2"), 1, 1, 1, 1)
    layout.addWidget(QRadioButton("optionA"), 2, 0, 1, 1)
    layout.addWidget(QRadioButton("optionB"), 2, 1, 1, 1)

    layout.addWidget(QLabel("Enter Line:"), 3, 0, 1, 1)
    layout.addWidget(QLineEdit(), 3, 2, 1, 1)

    self.setTabText(1,"Character")
    self.tab2.setLayout(layout)
