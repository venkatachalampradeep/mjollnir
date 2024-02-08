import os
from image_handler import ImageHandler
from photo_editor import PhotoEditor

def move_images_to_archive(src_folder, archive_folder):
    """Moves image files from the source folder to the archive folder."""
    files = os.listdir(src_folder)
    image_files = [file for file in files if file.lower().endswith((".jpg", ".jpeg"))]

    for image_file in image_files:
        src_image_path = os.path.join(src_folder, image_file)
        archive_image_path = os.path.join(archive_folder, image_file)
        os.rename(src_image_path, archive_image_path)

def delete_images_in_folder(folder):
    """Deletes all image files in the specified folder."""
    files = os.listdir(folder)
    image_files = [file for file in files if file.lower().endswith((".jpg", ".jpeg"))]
    for image_file in image_files:
        os.remove(os.path.join(folder, image_file))

def process_images_in_folder(src_folder, tgt_folder):
    """Processes images by adding padding and border, then saves them in the target folder."""
    files = os.listdir(src_folder)
    image_files = [file for file in files if file.lower().endswith((".jpg", ".jpeg"))]

    for image_file in image_files:
        input_image_path = os.path.join(src_folder, image_file)
        output_image_path = os.path.join(tgt_folder, image_file)

        image_handler = ImageHandler(input_image_path)
        image_handler.open_image()
        photo_editor = PhotoEditor(image_handler)

        edited_image = photo_editor.add_padding_and_border()

        if edited_image:
            edited_image.save(output_image_path)
        image_handler.close_image()

def stack_images_in_folder(src_folder, tgt_folder, stack_dir_vert):
    """Stacks images vertically or horizontally and saves the result in the target folder."""
    files = os.listdir(src_folder)
    image_files = [file for file in files if file.lower().endswith((".jpg", ".jpeg"))]

    image_files.sort()
    input_paths = [os.path.join(src_folder, image_file) for image_file in image_files]
    output_path = os.path.join(tgt_folder, "stacked_image.jpg")

    if stack_dir_vert:
        stacked_image = PhotoEditor.stack_images_vertically(input_paths)
    else:
        stacked_image = PhotoEditor.stack_images_horizontally(input_paths)

    if stacked_image:
        stacked_image.save(output_path)