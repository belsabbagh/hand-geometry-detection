import cv2

from src.img_ops.get_shape import ImageShape


def get_shape(img):
    """
    Gets a dictionary of the image's shape
    """
    return ImageShape(img)


def read_img(file_path, color_mode=None):
    if color_mode is None:
        color_mode = cv2.IMREAD_UNCHANGED
    return cv2.imread(file_path, color_mode)


def read_img_color(file_path):
    return read_img(file_path, cv2.IMREAD_COLOR)


def read_img_grayscale(file_path):
    return read_img(file_path, cv2.IMREAD_GRAYSCALE)


def create_haar_cascade_classifier(classifier_file_path):
    return cv2.CascadeClassifier(classifier_file_path)
