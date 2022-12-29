"""
This module contains the functions to draw the geometry of the hand on an image
"""
import cv2
from cv2.mat_wrapper import Mat

from src.hand_detector.hand_shape import HandShape
from src.image_ops import draw_contours


def draw_hand_geometry(img: Mat, hand: HandShape) -> Mat:
    """Draw the geometry of the hand on an image

    Args:
        img (Mat): The image to draw on
        hand (hand): The hand

    Returns:
        Mat: The image with the geometry drawn
    """
    if len(hand.points) >= 4:
        draw_contours(img, [hand.contour], (0, 255, 0), 2)
        draw_contours(img, [hand.hull], (0, 0, 255), 3)
        for pt in hand.points:
            cv2.circle(img, pt, 8, [211, 84, 0], -1)
    return img
