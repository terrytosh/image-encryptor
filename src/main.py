from PyQt5.QtWidgets import *
from MainGUI import MainGUI

def main():
    app = QApplication([])
    window = MainGUI()
    window.setWindowTitle("Terry's Image Encryptor!")
    app.exec_()

if __name__ == '__main__':
    main()
