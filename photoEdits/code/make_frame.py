import os
from image_handler import ImageHandler
from photo_editor import PhotoEditor
from datetime import datetime

def move_images_to_archive(src_folder, archive_folder):
    files = os.listdir(src_folder)
    image_files = [file for file in files if file.lower().endswith((".jpg", ".jpeg"))]

    for image_file in image_files:
        src_image_path = os.path.join(src_folder, image_file)
        archive_image_path = os.path.join(archive_folder, image_file)
        os.rename(src_image_path, archive_image_path)

def process_images_in_folder(input_folder, output_folder):
    files = os.listdir(input_folder)
    image_files = [file for file in files if file.lower().endswith((".jpg", ".jpeg"))]

    for image_file in image_files:
        input_image_path = os.path.join(input_folder, image_file)
        output_image_path = os.path.join(output_folder, image_file)

        image_handler = ImageHandler(input_image_path)
        image_handler.open_image()
        photo_editor = PhotoEditor(image_handler)

        # Python function to add padding and frames
        new_image = photo_editor.add_padding_and_border(output_path=output_image_path)

        new_image.save(output_image_path)
        image_handler.close_image()

if __name__ == "__main__":
    src_folder = "../src/"
    tgt_folder = "../tgt/"
    archive_folder = "../archive/"

    # Move existing pictures to the archive folder
    # move_images_to_archive(src_folder, archive_folder)

    # Process images in the src folder (which is now empty)
    process_images_in_folder(src_folder, tgt_folder)
