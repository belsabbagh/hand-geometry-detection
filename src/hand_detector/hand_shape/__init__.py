import cv2

from src.hand_detector.hand_shape.finger_detector import find_fingers, found_fingers
from src.image_ops import get_convex_hull


class NotAHandException(Exception):
    """Raised when the shape isn't a hand"""
    pass


class HandShape:
    def __init__(self, contour, hull=None):
        status, points = find_fingers(contour)
        if not found_fingers(status, points):
            raise NotAHandException
        self.contour = contour
        self.points = points
        self.hull = hull if hull is not None else get_convex_hull(contour)
        self.area = cv2.contourArea(self.contour)
