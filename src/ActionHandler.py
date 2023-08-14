class ActionHandler:
    def __init__(self, selected_image_file, output_directory):
        self.selected_image_file = selected_image_file
        self.output_directory = output_directory

    def handle_encryption(self, algorithm):
        print("Handling Encryption with", algorithm)
        # Implement your encryption logic here

    def handle_decryption(self, algorithm):
        print("Handling Decryption with", algorithm)
        # Implement your decryption logic here