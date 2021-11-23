import sys
import random

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton(self)
        self.button.setGeometry(10, 10, 30, 50)
        self.setGeometry(100, 100, 700, 700)


class MyWidget(Example):
    def __init__(self):
        super().__init__()
        self.button.clicked.connect(self.paint)
        self.do_paint = False

    def draw_el(self, qp):
        self.a = random.randint(30, 100)
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        qp.drawEllipse(random.randint(81, 650), random.randint(81, 650), self.a, self.a)


    def paintEvent(self, event):
        if not self.do_paint:
            return
        self.do_paint = False
        qp = QPainter()
        qp.begin(self)
        self.draw_el(qp)
        qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
