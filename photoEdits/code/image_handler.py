from PIL import Image

class ImageHandler:
    """Handles basic image operations like opening, closing, and saving images using PIL."""
    
    def __init__(self, image_path):
        """Initializes the ImageHandler with a path to an image."""
        self.image_path = image_path
        self.image = None

    def open_image(self):
        """Opens the image from the path set at initialization."""
        self.image = Image.open(self.image_path)

    def close_image(self):
        """Closes the image if it is open, freeing resources."""
        if self.image:
            self.image.close()
            self.image = None

    def save_image(self, output_path):
        """Saves the open image to the specified output path."""
        if self.image:
            self.image.save(output_path)

    @property
    def dimensions(self):
        """Returns the dimensions of the open image if available."""
        return self.image.size if self.image else None
