"""
This module contains the finger detector
"""

import math

import cv2
import numpy as np


def find_fingers(contour: np.ndarray) -> tuple[bool, list | None]:
    """Find the shape of fingers of a hand from a contour

    Args:
        contour (np.ndarray): The contour of the hand

    Returns:
        tuple[bool, list|None]: A tuple with a boolean indicating if the contour is a hand
        and a list of points of the connection between fingers.
    """
    hull = cv2.convexHull(contour, returnPoints=False)
    if len(hull) <= 3:
        return False, None
    defects = cv2.convexityDefects(contour, hull)
    if defects is None:
        return False, None
    points = [pt for angle, pt in [calculate_angle_from_defect(d[0], contour) for d in defects] if angle <= math.pi / 2]
    return (True, points) if len(points) > 0 else (False, None)


def calculate_angle(start: tuple[int, int], end: tuple[int, int], far: tuple[int, int]) -> float:
    """Calculate the angle using cosine theorem

    Args:
        start (tuple[int,int]): Start point of the line
        end (tuple[int,int]): End point of the line
        far (tuple[int,int]): Point to calculate the angle

    Returns:
        float: Angle in radians at far point
    """
    a = math.dist(start, end)
    b = math.dist(start, far)
    c = math.dist(end, far)
    return math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))


def calculate_angle_from_defect(defect: np.ndarray, contour: np.ndarray) -> tuple[float, tuple[int, int]]:
    """Calculate the angle of a convexity defect

    Args:
        defect (np.ndarray): The convexity defect to calculate the angle for
        contour (np.ndarray): The contour of the hand

    Returns:
        tuple[float, tuple[int, int]]: The angle in radians and the far point
    """
    s, e, f, _ = defect
    start = tuple(contour[s][0])
    end = tuple(contour[e][0])
    far = tuple(contour[f][0])
    return calculate_angle(start, end, far), far


def found_fingers(status, points):
    return status is True and points is not None
