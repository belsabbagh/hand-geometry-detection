"""
A module that has a helper function that helps with scaling images.
"""

import cv2


def scale_img(img, scale_coefficient: float):
    """

    :param img: The given image
    :type img:
    :param scale_coefficient: The value to multiply scale by
    :type scale_coefficient: float
    :return: The resized image
    :rtype:
    """
    width = int(img.shape[1] * scale_coefficient)
    height = int(img.shape[0] * scale_coefficient)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)


def resize_img(img, width, height):
    return cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
