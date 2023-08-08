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

        # Connect 'Execute Action' button to handle_execute_action_button_cliked()
        self.execute_action_button.clicked.connect(self.handle_execute_action_button_clicked)

        # Connect 'Select Output Directory' button to handle_select_output_directory_button_clicked()
        self.select_output_directory_button.clicked.connect(self.handle_select_output_directory_button_clicked)

    def handle_execute_action_button_clicked(self):
        # Print current selections from QComboBox's
        print(self.action_selection_box.currentText())
        print(self.algorithm_selection_box.currentText())
    
    def handle_select_output_directory_button_clicked(self):
        print("Handling output direction selection...")
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog
        output_directory = QFileDialog.getExistingDirectory(self, "Select Output Directory", options=options)

        if output_directory:
            print("Selected Output Directory:", output_directory)
            # Here, you can use the selected directory for saving your data