#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, Qt, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QDialog, QMessageBox
from PyQt5.QtGui import QPainter, QPen


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Viewer2DWidget(QWidget):
    keyPressed = QtCore.pyqtSignal(QtCore.QEvent)

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setMouseTracking(True)
        self.isPressed = False
        self.oldx = self.oldy = 0
        self.keyPressed.connect(self.on_key)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setFocus(QtCore.Qt.PopupFocusReason)
        self.start()

        self.width = 70
        self.height = 70
        self.is_wasted = False
        # self.setEnabled(True)

    def start(self):
        self.motocycle = Coord(34, 1)
        self.motocycle_speed = Coord(0, 1)
        self.trail = []

        # https://www.developpez.net/forums/d1953793/autres-langages/python/gui/pyqt/qtimer-repetitions/
        self.timer = QtCore.QTimer()
        self.timer.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer.setInterval(70)
        self.timer.timeout.connect(self.move_moto)
        self.timer.start()

    def move_moto(self):
        self.trail.append(Coord(self.motocycle.x, self.motocycle.y))
        self.motocycle.x = self.motocycle.x + self.motocycle_speed.x
        self.motocycle.y = self.motocycle.y + self.motocycle_speed.y

        if self.motocycle.x < 0 or self.motocycle.x >= self.width or self.motocycle.y < 0 or self.motocycle.y >= self.height:
            self.is_wasted = True
            print("wasted")
            self.timer.stop()
            # https://www.tutorialspoint.com/pyqt/pyqt_qmessagebox.htm
            message_box = QMessageBox(self)
            message_box.setIcon(QMessageBox.Information)

            message_box.setText("Wasted")
            message_box.setInformativeText("Do you want to restart a game?")
            message_box.setWindowTitle("Wasted")
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.show()
            self.start()

        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setWindow(0, 0, self.width, self.height)

        painter.fillRect(0, 0, self.width, self.height, QtCore.Qt.black)
        painter.fillRect(self.motocycle.x, self.motocycle.y,
                         1, 1, QtCore.Qt.green)

        for position in self.trail:
            painter.fillRect(position.x, position.y,
                             1, 1, QtCore.Qt.red)

    def mouseDoubleClickEvent(self, mouseEvent):
        print("double click")

    def on_key(self, event):
        print("key press")
        print(event.text())

    def keyPressEvent(self, event):
        print("key press")
        if event.key() == 16777235:  # up
            self.motocycle_speed.x = 0
            self.motocycle_speed.y = -1
        elif event.key() == 16777237:  # down
            self.motocycle_speed.x = 0
            self.motocycle_speed.y = 1
        elif event.key() == 16777236:  # right
            self.motocycle_speed.x = 1
            self.motocycle_speed.y = 0
        elif event.key() == 16777234:  # left
            self.motocycle_speed.x = -1
            self.motocycle_speed.y = 0

    def mousePressEvent(self, e):
        print("mouse press")
        self.isPressed = True
        painter = QPainter(self)
        painter.drawArc(QtCore.QRectF(10, 10, 50, 50), 0, 5760)

    def mouseReleaseEvent(self, e):
        print("mouse release")
        self.isPressed = False


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

container = Viewer2DWidget(window)

container.setFixedHeight(800)
container.setFixedWidth(800)

layout.addWidget(container)
window.setLayout(layout)
window.show()
app.exec_()
