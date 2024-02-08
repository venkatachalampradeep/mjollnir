import argparse
import utils  # Import the utilities from utils.py

def main():
    parser = argparse.ArgumentParser(description="Image processing options")
    parser.add_argument("--operation", choices=["add_padding_and_border", "stack_images_horz", "stack_images_vert", "clean_folders", "archive_and_clean"], required=True, help="Choose the operation")
    parser.add_argument("--src_folder", required=False, default="../src/", help="Source folder path")
    parser.add_argument("--tgt_folder", required=False, default="../tgt/", help="Target folder path")
    parser.add_argument("--archive_folder", required=False, default="../archive/", help="Archive folder path")

    args = parser.parse_args()

    if args.operation == "add_padding_and_border":
        utils.process_images_in_folder(args.src_folder, args.tgt_folder)
    elif args.operation == "stack_images_vert":
        utils.stack_images_in_folder(args.src_folder, args.tgt_folder, True)
    elif args.operation == "stack_images_horz":
        utils.stack_images_in_folder(args.src_folder, args.tgt_folder, False)
    elif args.operation == "clean_folders":
        utils.delete_images_in_folder(args.src_folder)
        utils.delete_images_in_folder(args.tgt_folder)
    elif args.operation == "archive_and_clean":
        utils.move_images_to_archive(args.tgt_folder, args.archive_folder)
        utils.delete_images_in_folder(args.src_folder)
        utils.delete_images_in_folder(args.tgt_folder)

if __name__ == "__main__":
    main()
