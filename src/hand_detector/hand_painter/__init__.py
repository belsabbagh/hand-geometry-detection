import cv2

from src.image_ops import draw_contours


def draw_hand_geometry(img, hull, points, res):
    if len(points) >= 4:
        draw_contours(img, [res], (0, 255, 0), 2)
        draw_contours(img, [hull], (0, 0, 255), 3)
        for pt in points:
            cv2.circle(img, pt, 8, [211, 84, 0], -1)
    return img
