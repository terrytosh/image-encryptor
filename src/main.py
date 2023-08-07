import os
from PyQt5.QtWidgets import *
from PyQt5 import uic

class MainGUI(QMainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()
        ui_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mainwindow.ui")
        uic.loadUi(ui_file, self)
        self.show()

def main():
    app = QApplication([])
    window = MainGUI()
    window.setWindowTitle("Terry's Image Encryptor!")
    app.exec_()

if __name__ == '__main__':
    main()
