"""
This module contains the functions to draw the geometry of the hand on an image
"""
import cv2
import numpy as np
from cv2.mat_wrapper import Mat

from src.image_ops import draw_contours


def draw_hand_geometry(img: Mat, hull: np.ndarray, points: list, contour: np.ndarray) -> Mat:
    """Draw the geometry of the hand on an image

    Args:
        img (Mat): The image to draw on
        hull (np.ndarray): The hull of the hand
        points (list): The points of the fingers
        contour (np.ndarray): The contour of the hand

    Returns:
        Mat: The image with the geometry drawn
    """
    if len(points) >= 4:
        draw_contours(img, [contour], (0, 255, 0), 2)
        draw_contours(img, [hull], (0, 0, 255), 3)
        for pt in points:
            cv2.circle(img, pt, 8, [211, 84, 0], -1)
    return img
