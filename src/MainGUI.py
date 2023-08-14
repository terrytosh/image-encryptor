from PyQt5.QtWidgets import *
from PyQt5 import uic
from ActionHandler import ActionHandler

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

        # Initialize instance variables
        self.selected_image_file = ""
        self.output_directory = ""

    def handle_execute_action(self):
        # Store user inputs actions
        current_action = self.action_selection_box.currentText()
        current_algorithm = self.algorithm_selection_box.currentText()

        # Check for valid user input
        if self.selected_image_file == "" or self.output_directory == "":
            QMessageBox.warning(self, "Error!", "Select image file and output directory.")
        elif self.keyPasswordLineEdit.text() == "":
            QMessageBox.warning(self, "Error!", "Please provide a key/password.")
        else:
            # Handle encryption
            if current_action == "Encryption":
                action_handler = ActionHandler(self.selected_image_file, self.output_directory)
                action_handler.handle_encryption(current_algorithm)
            # Handle decryption
            elif current_action == "Decryption":
                action_handler = ActionHandler(self.selected_image_file, self.output_directory)
                action_handler.handle_decryption(current_algorithm)
                    


    def handle_file_select(self):
        # print("Handling file selection...")
        options = QFileDialog.Options() # Creation 'Options' objects
        options |= QFileDialog.ReadOnly # Force user to only select already existing files
        file_filter = "Images (*.jpg *.png)" # User can only select .jpg and .png file types

        # store path of selected image file
        selected_image_file, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", file_filter, options=options)

        if selected_image_file:
            # print("Selected Image File:", selected_image_file)
            self.selected_image_file = selected_image_file
            self.selected_file_label.setText(selected_image_file) # Modify label to show path of selected image file
        else:
            QMessageBox.warning(self, "Warning!", "No image file was selected.") # Warn user that no image file was selected
 
    
    def handle_select_output_directory(self):
        # print("Handling output direction selection...")
        options = QFileDialog.Options() # Creation 'Options' objects
        options |= QFileDialog.ShowDirsOnly # Show only directories
        output_directory = QFileDialog.getExistingDirectory(self, "Select Output Directory", options=options)

        if output_directory:
            # print("Selected Output Directory:", output_directory)
            self.output_directory = output_directory
            self.selected_output_directory_label.setText(output_directory)
        else:
            QMessageBox.warning(self, "Warning!", "No output directory was selected.")