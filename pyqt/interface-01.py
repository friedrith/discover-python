#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel('Hello world!')
label.show()
app.exec_()
