import cv2

from src.image_ops import draw_contours


def draw_hand_geometry(drawing, hull, points, res):
    draw_contours(drawing, [res], (0, 255, 0), 2)
    draw_contours(drawing, [hull], (0, 0, 255), 3)
    for pt in points:
        cv2.circle(drawing, pt, 8, [211, 84, 0], -1)
    return drawing
