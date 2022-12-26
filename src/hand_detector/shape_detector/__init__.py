import cv2
import numpy as np


def get_hand_shapes_from_contours(contours):
    return [(i, cv2.convexHull(i)) for i in contours]


def get_largest_shape(shapes: list[tuple[np.ndarray, int]]) -> np.ndarray:
    """Get the largest contour from a list of contours

    Args:
        shapes (list[tuple[np.ndarray, int]]): A list of tuples of hand contour and hull.

    Returns:
        np.ndarray: The largest contour
    """
    largest_contour = max([(i, cv2.contourArea(i)) for i, _ in shapes], key=lambda item: item[1])
    return largest_contour[0]
