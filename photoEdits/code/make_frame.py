import os
import argparse
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

def process_images_in_folder(src_folder, tgt_folder):
    files = os.listdir(src_folder)
    image_files = [file for file in files if file.lower().endswith((".jpg", ".jpeg"))]

    for image_file in image_files:
        input_image_path = os.path.join(src_folder, image_file)
        output_image_path = os.path.join(tgt_folder, image_file)

        image_handler = ImageHandler(input_image_path)
        image_handler.open_image()
        photo_editor = PhotoEditor(image_handler)

        edited_image = photo_editor.add_padding_and_border()  # Get the edited image

        if edited_image:
            edited_image.save(output_image_path)  # Save the edited image
        image_handler.close_image()

def stack_images_in_folder(src_folder, tgt_folder, stack_dir_vert):
    files = os.listdir(src_folder)
    image_files = [file for file in files if file.lower().endswith((".jpg", ".jpeg"))]

    image_files.sort()

    # Take the first three images for stacking
    input_paths = [os.path.join(src_folder, image_files[i]) for i in range(len(image_files))]
    output_path = os.path.join(tgt_folder, "stacked_image.jpg")

    if stack_dir_vert:
        stacked_image = PhotoEditor.stack_images_vertically(input_paths)
    else:
        stacked_image = PhotoEditor.stack_images_horizontally(input_paths)
    
    if stacked_image:
        stacked_image.save(output_path)  # Save the stacked image

if __name__ == "__main__":
    src_folder = "../src/"
    tgt_folder = "../tgt/"
    parser = argparse.ArgumentParser(description="Image processing options")
    parser.add_argument("--operation", choices=["add_padding_and_border", "stack_images_horz", "stack_images_vert"], required=True, help="Choose the image processing operation")

    args = parser.parse_args()

    if args.operation == "add_padding_and_border":
        process_images_in_folder(src_folder, tgt_folder)
    elif args.operation == "stack_images_vert":
        stack_images_in_folder(src_folder, tgt_folder, stack_dir_vert=True)
    elif args.operation == "stack_images_horz":
        stack_images_in_folder(src_folder, tgt_folder, stack_dir_vert=False)