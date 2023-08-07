from PyQt5.QtWidgets import *
from PyQt5 import uic
import os

class MainGUI(QMainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()

        # Create file path to UI file
        ui_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mainwindow.ui")
        uic.loadUi(ui_file, self)

        # Display 'mainwindow' UI
        self.show()

        # Quit app when 'Exit' clicked in the toolbar
        self.exit_action.triggered.connect(qApp.quit)

        print("From MainGUI...")
        
        # Connect 'Execute Action' button to on_execute_action_button_cliked() function
        self.execute_action_button.clicked.connect(self.on_execute_action_button_clicked)

    def on_execute_action_button_clicked(self):
        print("Execute action button clicked...")