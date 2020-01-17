from PyQt5 import QtCore, QtGui, Qt, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPainter, QPen


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

container = QWidget()

container.setFixedHeight(800)
container.setFixedWidth(800)

painter = QPainter(container)
painter.setPen(QPen(QtCore.Qt.red))
painter.drawArc(QtCore.QRectF(150, 150, 50, 50), 0, 5760)

layout.addWidget(container)
window.setLayout(layout)
window.show()
app.exec_()
