from Xor import Xor
import os

class ActionHandler:
    def __init__(self, selected_image_file, output_directory):
        self.selected_image_file = selected_image_file
        self.output_directory = output_directory

    def handle_encryption(self, algorithm):

        print("Handling Encryption with", algorithm)
        output_path = os.path.join(self.output_directory, "encrypted_image.png")

        if algorithm == "XOR":
            xor_encryptor = Xor(self.selected_image_file, output_path)
            xor_encryptor.encrypt()
            print("XOR Encryption complete. Encrypted image saved at:", output_path)

    def handle_decryption(self, algorithm):

        print("Handling Decryption with", algorithm)
        output_path = os.path.join(self.output_directory, "decrypted_image.png")

        if algorithm == "XOR":
            xor_decryptor = Xor(self.selected_image_file, output_path)
            xor_decryptor.decrypt()
            print("XOR Decryption complete. Decrypted image saved at:", output_path)