# Image Processing Utility

## Overview
This project provides a command-line interface for basic image processing tasks, such as adding padding and borders to images, stacking images, and managing image files between directories.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip for installing dependencies

### Installation

1. Clone the repository to your local machine:
2. Navigate to the project directory:
3. Install the required dependencies:

## Requirements
- Python 3.6+
- Pillow library

##  Usage

The `main.py` script supports several command-line arguments for processing images. Here is how you can use them:

- --operation: Specifies the operation to perform. Can be `add_padding_and_border`, `stack_images_horz`, or `stack_images_vert`.
- --src_folder: The path to the source folder containing images to process.
- --tgt_folder: The path to the target folder where processed images will be saved.

### Examples

Add padding and border to all images in a folder:
```bash
python main.py --operation add_padding_and_border --src_folder path/to/source --tgt_folder path/to/target
python3 main.py --operation archive_and_clean
```