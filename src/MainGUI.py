from PyQt5.QtWidgets import *
from PyQt5 import uic
import os

class MainGUI(QMainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()
        ui_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mainwindow.ui")
        uic.loadUi(ui_file, self)
        self.show()