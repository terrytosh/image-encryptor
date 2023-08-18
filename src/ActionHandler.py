from Xor import Xor
from PixelShuffler import PixelShuffler
import os

class ActionHandler:
    def __init__(self, selected_image_file, output_directory, key):
        self.selected_image_file = selected_image_file
        self.output_directory = output_directory
        self.key = key

    def handle_encryption(self, algorithm):

        print("Handling Encryption with", algorithm)
        output_path = os.path.join(self.output_directory, "encrypted_image.png")

        if algorithm == "XOR":
            xor_encryptor = Xor(self.selected_image_file, output_path, self.key)
            xor_encryptor.encrypt()
            print("XOR encryption complete. Encrypted image saved at:", output_path)
        elif algorithm == "Pixel Shuffling":
            pixel_shuffler = PixelShuffler(self.selected_image_file, output_path, self.key)
            pixel_shuffler.shuffle()
            print("Pixel shuffling encryption complete. Encrypted image saved at:", output_path)
        elif algorithm == "XOR with Shuffling":
            xor_encryptor = Xor(self.selected_image_file, output_path, self.key)
            xor_encryptor.encrypt()
            pixel_shuffler = PixelShuffler(self.selected_image_file, output_path, self.key)
            pixel_shuffler.shuffle()
            print("XOR with shuffling encryption complete. Encrypted image saved at:", output_path)

    def handle_decryption(self, algorithm):

        print("Handling Decryption with", algorithm)
        output_path = os.path.join(self.output_directory, "decrypted_image.png")

        if algorithm == "XOR":
            xor_decryptor = Xor(self.selected_image_file, output_path, self.key)
            xor_decryptor.decrypt()
            print("XOR Decryption complete. Decrypted image saved at:", output_path)
        elif algorithm == "Pixel Shuffling":
            pixel_shuffler = PixelShuffler(self.selected_image_file, output_path, self.key)
            pixel_shuffler.unshuffle()
            print("Pixel shuffling decryption complete. Decrypted image saved at:", output_path)
        elif algorithm == "XOR with Shuffling":
            xor_encryptor = Xor(self.selected_image_file, output_path, self.key)
            xor_encryptor.decrypt()
            pixel_shuffler = PixelShuffler(self.selected_image_file, output_path, self.key)
            pixel_shuffler.unshuffle()
            print("XOR with shuffling decryption complete. Encrypted image saved at:", output_path)