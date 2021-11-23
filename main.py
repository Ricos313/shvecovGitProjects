import sys
import random

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def draw_el(self, qp):
        qp.setBrush(QColor(255, 186, 0))
        qp.drawEllipse(random.randint(100, 200), random.randint(100, 200), random.randint(30, 100), random.randint(30, 100))


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
