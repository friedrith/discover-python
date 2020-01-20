#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


def button_top_clicked(mouseEvent):
    print("Button 1 clicked")


def button_bottom_clicked(mouseEvent):
    print("Button 2 clicked")


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

button_top = QPushButton('Top')
button_top.clicked.connect(button_top_clicked)

button_bottom = QPushButton('Bottom')
button_bottom.clicked.connect(button_bottom_clicked)

layout.addWidget(button_top)
layout.addWidget(button_bottom)

window.setLayout(layout)
window.show()
app.exec_()
