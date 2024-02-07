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
    
    @staticmethod
    def stack_images_vertically(image_paths):
        try:
            # Open the input images
            images = [Image.open(path) for path in image_paths]

            # Find the lowest width among the images
            min_width = min(image.width for image in images)

            # Calculate the height of the stacked image based on the aspect ratio
            total_height = sum(image.height * (min_width / image.width) for image in images)

            # Get the mode (color mode) from the first input image
            image_mode = images[0].mode

            # Create a new blank image with the desired dimensions (min_widthxtotal_height)
            stacked_image = Image.new(image_mode, (min_width, int(total_height)))

            # Paste the images on top of each other, resizing as needed
            y_offset = 0
            for image in images:
                # Calculate the new height to maintain aspect ratio
                new_height = int(image.height * (min_width / image.width))
                resized_image = image.resize((min_width, new_height))
                stacked_image.paste(resized_image, (0, y_offset))
                y_offset += new_height
            
            # Return the stacked image
            return stacked_image

        except Exception as e:
            print(f"Error: {str(e)}")
            return None

    @staticmethod
    def stack_images_horizontally(image_paths):
        try:
            # Open the input images
            images = [Image.open(path) for path in image_paths]

            # Find the total width of the stacked image
            total_width = sum(image.width for image in images)

            # Get the mode (color mode) from the first input image
            image_mode = images[0].mode

            # Calculate the height of the stacked image based on the tallest image
            max_height = max(image.height for image in images)

            # Create a new blank image with the desired dimensions and mode
            stacked_image = Image.new(image_mode, (total_width, max_height))

            # Paste the images side by side
            x_offset = 0
            for image in images:
                stacked_image.paste(image, (x_offset, 0))
                x_offset += image.width

            # Return the stacked image
            return stacked_image

        except Exception as e:
            print(f"Error: {str(e)}")
            return None
