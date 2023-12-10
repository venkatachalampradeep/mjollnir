from PIL import Image

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None

    def open_image(self):
        self.image = Image.open(self.image_path)

    def close_image(self):
        if self.image:
            self.image.close()
            self.image = None

    def save_image(self, output_path):
        if self.image:
            self.image.save(output_path)

    @property
    def dimensions(self):
        if self.image:
            return self.image.size
        return None
