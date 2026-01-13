import sys, pyfiglet

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Volleyball Stats Tracker")
        
        self.setFixedSize(QSize(1280, 800))
        
        widget = QLabel()
        #font = widget.font()
        #font.setPointSize(10)
        #widget.setFont(font)
        widget.setPixmap(QPixmap('volleyballtracker.png'))
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()