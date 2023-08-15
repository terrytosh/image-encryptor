from PIL import Image

class XorEncryptor:
    def __init__(self, selected_image_file, output_path):
        self.key = (255, 155, 55)  # Example key
        self.selected_image_file = selected_image_file
        self.output_path = output_path

    def encrypt(self):
        # Open the image file
        image = Image.open(self.selected_image_file)

        # Get pixel data as a list of tuples (R, G, B) for RGB images or (L,) for grayscale images
        pixel_data = list(image.getdata())

        # Perform XOR encryption on each pixel
        encrypted_pixel_data = []
        for pixel in pixel_data:
            encrypted_pixel = tuple([(p ^ k) for p, k in zip(pixel, self.key)])
            encrypted_pixel_data.append(encrypted_pixel)
        
        # Create a new image with encrypted pixel data
        encrypted_image = Image.new(image.mode, image.size)
        encrypted_image.putdata(encrypted_pixel_data)

        # Save the encrypted image to the specified output path
        encrypted_image.save(self.output_path)

        print(self.output_path)

        # Close the images
        image.close()
        encrypted_image.close()
    
    def decrypt(self, data):
        decrypted_data = bytes([b ^ 0x55 for b in data])
        return decrypted_data