import numpy as np

from src.gray_level_transformations import base_transform
from src.gray_level_transformations.base_transform import base_transform
from src.gray_level_transformations.gamma_correction import gamma_correction_function
from src.gray_level_transformations.log_transform import log_transform_function
from src.gray_level_transformations.negative_transform import negative_transformation_function
from src.gray_level_transformations.slice_gray_level import gray_level_slice_function
from src.gray_level_transformations.stretch_contrast import ignore_percentage, contrast_stretch_function


def binary_threshold(img, thr):
    return base_transform(img, gray_level_slice_function, 0, thr, False)


def inverse_binary_threshold(img, thr):
    return base_transform(negative_transform(img), gray_level_slice_function, 0, thr, False)


def correct_gamma(img, gamma, c=None):
    if c is None:
        c = 255 / (np.max(img) ** gamma)
    return base_transform(img, gamma_correction_function, gamma, c)


def log_transform(img, c):
    return base_transform(img, log_transform_function, c)


def negative_transform(img):
    return base_transform(img, negative_transformation_function)


def slice_gray_level(img, min_thr, max_thr, keep=False):
    return base_transform(img, gray_level_slice_function, min_thr, max_thr, keep)


def stretch_contrast(img, r_min=None, r_max=None, s_min=0, s_max=255):
    if r_min is None and r_max is None:
        r_min, r_max = ignore_percentage(img, 0.15)
    return base_transform(img, contrast_stretch_function, r_min, r_max, s_min, s_max)
