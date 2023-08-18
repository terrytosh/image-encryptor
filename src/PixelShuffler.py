from PIL import Image
import random

class PixelShuffler:
    def __init__(self, selected_image_file, output_path):
        self.key = "secret_shuffling_key"  # Example key
        self.selected_image_file = selected_image_file
        self.output_path = output_path

    def shuffle(self):
        # Open the image file
        image = Image.open(self.selected_image_file)
        width, height = image.size
        pixel_map = image.load()

        # Create a new shuffled image
        shuffled_image = Image.new("RGB", (width, height))
        shuffled_pixels = shuffled_image.load()

        # Generate shuffled indices
        index_list = list(range(width * height))
        random.seed(self.key)
        random.shuffle(index_list)

        # Populate shuffled image with pixels from the original image
        for i in range(width):
            for j in range(height):
                shuffled_index = index_list[i * height + j]
                x = shuffled_index // height
                y = shuffled_index % height
                shuffled_pixels[i, j] = pixel_map[x, y]

        # Save the shuffled image to the output path
        shuffled_image.save(self.output_path)

        # Close the opened images to release resources
        image.close()
        shuffled_image.close()

    def unshuffle(self):
        # Open the shuffled image file
        shuffled_image = Image.open(self.selected_image_file)
        width, height = shuffled_image.size
        shuffled_pixel_map = shuffled_image.load()

        # Create a new image for unshuffled pixels
        unshuffled_image = Image.new("RGB", (width, height))
        unshuffled_pixels = unshuffled_image.load()

        # Generate shuffled indices
        index_list = list(range(width * height))
        random.seed(self.key)
        shuffled_indices = index_list[:]
        random.shuffle(shuffled_indices)

        # Populate unshuffled image with pixels from the shuffled image
        for i in range(width):
            for j in range(height):
                shuffled_index = shuffled_indices[i * height + j]
                x = shuffled_index // height
                y = shuffled_index % height
                unshuffled_pixels[x, y] = shuffled_pixel_map[i, j]

        # Save the unshuffled image to the output path
        unshuffled_image.save(self.output_path)

        # Close the opened images to release resources
        shuffled_image.close()
        unshuffled_image.close()