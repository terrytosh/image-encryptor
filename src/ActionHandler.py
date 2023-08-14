from XorEncryptor import XorEncryptor
import os

class ActionHandler:
    def __init__(self, selected_image_file, output_directory):
        self.selected_image_file = selected_image_file
        self.output_directory = output_directory

    def handle_encryption(self, algorithm):
        print("Handling Encryption with", algorithm)
        if algorithm == "XOR":
            with open(self.selected_image_file, 'rb') as file:
                image_data = file.read()

            xor_encryptor = XorEncryptor()
            encrypted_data = xor_encryptor.encrypt(image_data)

            output_path = os.path.join(self.output_directory, "encrypted_image.png")
            with open(output_path, 'wb') as file:
                file.write(encrypted_data)

            print("XOR Encryption complete. Encrypted image saved at:", output_path)

    def handle_decryption(self, algorithm):
        print("Handling Decryption with", algorithm)
        if algorithm == "XOR":
            with open(self.selected_image_file, 'rb') as file:
                image_data = file.read()
            
            xor_encryptor = XorEncryptor()
            decrypted_data = xor_encryptor.decrypt(image_data)

            output_path = os.path.join(self.output_directory, "decrypted_image.png")
            with open(output_path, 'wb') as file:
                file.write(decrypted_data)

            print("XOR Decryption complete. Decrypted image saved at:", output_path)