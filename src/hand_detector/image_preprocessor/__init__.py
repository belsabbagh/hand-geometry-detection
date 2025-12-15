"""
This module is responsible for preprocessing the image before the detection starts.
"""

import cv2

from src.image_ops import mask_color, bilateral_filter


def preprocess(_img):
    """
    The image is blurred using a bilateral filter which does great
    blurring while preserving edges for further segmentation.
    The image is then binarized using a color mask that masks the skin colors.
    """
    result = binarize_skin(_img)
    return result


def binarize_skin(img):
    return mask_color(img, [0, 48, 80], [20, 255, 255])
