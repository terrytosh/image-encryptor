from PyQt5.QtWidgets import *
from PyQt5 import uic
import os

class MainGUI(QMainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()

        # Load UI from 'src'mainwindow.ui'
        uic.loadUi("src/mainwindow.ui", self)

        # Display 'mainwindow' UI
        self.show()

        # Quit app when 'Exit' QAction clicked in the toolbar
        self.exit_action.triggered.connect(qApp.quit)

        # Connect 'Execute Action' button to on_execute_action_button_cliked() function
        self.execute_action_button.clicked.connect(self.handle_execute_action_button_clicked)

    def handle_execute_action_button_clicked(self):
        # Print current selections from QComboBox's
        print(self.action_selection_box.currentText())
        print(self.algorithm_selection_box.currentText())