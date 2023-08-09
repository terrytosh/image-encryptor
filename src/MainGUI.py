from PyQt5.QtWidgets import *
from PyQt5 import uic

class MainGUI(QMainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()
        
        # Load UI from 'src'mainwindow.ui'
        uic.loadUi("src/mainwindow.ui", self)

        # Display 'mainwindow' UI
        self.show()

        # Quit app when 'Exit' QAction clicked in the toolbar
        self.exit_action.triggered.connect(qApp.quit)

        # Connect 'Execute Action' button to handle_execute_action()
        self.execute_action_button.clicked.connect(self.handle_execute_action)

        self.file_select_button.clicked.connect(self.handle_file_select)

        # Connect 'Select Output Directory' button to handle_select_output_directory()
        self.select_output_directory_button.clicked.connect(self.handle_select_output_directory)

    def handle_execute_action(self):
        # Print current selections from QComboBox's
        print(self.action_selection_box.currentText())
        print(self.algorithm_selection_box.currentText())

    def handle_file_select(self):
        print("Handling file selection...")
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        selected_image_file = QFileDialog.getOpenFileName(self, "Open Image File", options=options)

        if selected_image_file:
            print("Selected Image File:", selected_image_file)
            # Here, you can use the selected directory for saving your data
    
    def handle_select_output_directory(self):
        print("Handling output direction selection...")
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly | QFileDialog.DontUseNativeDialog
        output_directory = QFileDialog.getExistingDirectory(self, "Select Output Directory", options=options)

        if output_directory:
            print("Selected Output Directory:", output_directory)
            # Here, you can use the selected directory for saving your data