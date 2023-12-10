from PIL import Image, ImageOps, ImageDraw, ImageFont

class PhotoEditor:
    def __init__(self, image_handler):
        self.image_handler = image_handler

    def add_padding_and_border(self, border_size=10, border_color=(255, 255, 255)):
        if self.image_handler.image:
            original_image = self.image_handler.image
            bordered_image = ImageOps.expand(original_image, border_size, fill=border_color)
        # Calculate padding and create a new image
        if self.image_handler.dimensions[0] < self.image_handler.dimensions[1]:
            desired_width = (bordered_image.height * 4) // 5
            padding_left = (desired_width - bordered_image.width) // 2
            new_image = Image.new(bordered_image.mode, (desired_width, bordered_image.height), (61, 61, 61))
            new_image.paste(bordered_image, (padding_left, 0))
        else:
            desired_height = (bordered_image.width * 5) // 4
            padding_top = (desired_height - bordered_image.height) // 2
            new_image = Image.new(bordered_image.mode, (bordered_image.width, desired_height), (61, 61, 61))
            new_image.paste(bordered_image, (0, padding_top))

        # Return the resulting image
        return new_image