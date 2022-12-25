import cv2
import numpy as np


def morph(img, mode, kernel=None, kernel_size=None):
    if kernel is None and kernel_size is not None:
        kernel = np.ones(kernel_size, np.uint8)
    return cv2.morphologyEx(img, mode, kernel)


def morph_open(img, kernel=None, kernel_size=None):
    return morph(img, cv2.MORPH_OPEN, kernel, kernel_size)


def morph_close(img, kernel=None, kernel_size=None):
    return morph(img, cv2.MORPH_CLOSE, kernel, kernel_size)


def morph_gradient(img, kernel=None, kernel_size=None):
    return morph(img, cv2.MORPH_GRADIENT, kernel, kernel_size)
