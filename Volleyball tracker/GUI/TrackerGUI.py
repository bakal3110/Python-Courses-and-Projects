import sys, pyfiglet

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QColor, QPalette
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Volleyball Stats Tracker")
        self.setFixedSize(QSize(1280, 800))

        pagelayout = QVBoxLayout()
        title_layout = QHBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()
        
        pagelayout.addLayout(title_layout)
        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)
        
        title_widget = QLabel()
        title_widget.setPixmap(QPixmap('volleyballtracker.png'))
        title_widget.setAlignment(Qt.AlignHCenter)
        title_layout.addWidget(title_widget)

        btn = QPushButton("red")
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("red"))

        btn = QPushButton("green")
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("green"))

        btn = QPushButton("yellow")
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stacklayout.addWidget(Color("yellow"))

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def activate_tab_1(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stacklayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stacklayout.setCurrentIndex(2)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
