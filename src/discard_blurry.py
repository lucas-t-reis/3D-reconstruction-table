import os
import cv2
import numpy as np

def variance_of_laplacian(image):
    """Compute the Laplacian of the image and then return the focus
    measure, which is simply the variance of the Laplacian."""
    return cv2.Laplacian(image, cv2.CV_64F).var()

def is_blurry(image_path, threshold=100.0):
    """Return True if the image is blurry."""
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    return fm < threshold

def discard_blurry_images(folder_path, threshold=100.0):
    """Print the paths of sharp images and discard (delete) blurry images."""
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            if is_blurry(image_path, threshold):
                print(f'Discarding {image_path}')
                os.remove(image_path)
            else:
                print(f'Keeping {image_path}')

# usage:
discard_blurry_images('imgs_path')