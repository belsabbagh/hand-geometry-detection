import numpy as np


def get_image_min_max_levels(img):
    return np.min(img), np.max(img)