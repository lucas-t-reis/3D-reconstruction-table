import os
import cv2

def create_video(folder_path, output_filename='output2.mp4', fps=14):
    """Create a video from .png images in a folder."""

    # Get the paths of all .png images in the folder, sorted by name
    image_paths = sorted([
        os.path.join(folder_path, filename)
        for filename in os.listdir(folder_path)
        if filename.endswith(".png")
    ])

    # Ensure there are images in the list
    if len(image_paths) == 0:
        print("No images found in the folder.")
        return

    # Get the size of the first image
    first_image = cv2.imread(image_paths[0])
    height, width, layers = first_image.shape
    size = (width, height)

    # Initialize a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or use 'XVID'
    out = cv2.VideoWriter(output_filename, fourcc, fps, size)

    # Iterate over images and add them to the video
    for image_path in image_paths:
        image_frame = cv2.imread(image_path)
        out.write(image_frame)

    out.release()

# usage:
create_video('C:\\Users\\lucas\\Downloads\\bags\pngs\\3\\')
